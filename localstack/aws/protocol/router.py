from collections import defaultdict
from typing import Any, Dict, List, Mapping, NamedTuple, Optional, Tuple
from urllib.parse import parse_qs, urlparse

from botocore.model import OperationModel, ServiceModel
from werkzeug.exceptions import NotFound
from werkzeug.routing import Map, MapAdapter, Rule

from localstack.http import Request


class QueryArgsRule:
    endpoint: Any
    parameters: Dict[str, List[Any]]

    def __init__(self, endpoint: Any, query_string: Optional[str]) -> None:
        super().__init__()
        self.endpoint = endpoint
        self.parameters = parse_qs(query_string) if query_string else {}

    def matches(self, query_string: Dict[str, List[str]]) -> bool:
        for key, values in self.parameters.items():
            if key not in query_string:
                return False
            if values != query_string[key]:
                return False

        return True

    def __str__(self):
        return f"{self.endpoinname}({self.parameters})"


class QueryArgsTreeRule(Rule):
    def __init__(self, string: str, *args, query_rules: List[QueryArgsRule], **kwargs) -> None:
        super().__init__(string, *args, **kwargs)
        self.query_rules = query_rules

    def match_query(self, query_string: str) -> QueryArgsRule:
        params = parse_qs(query_string) if query_string else {}

        default = None

        for rule in self.query_rules:
            if not rule.parameters:
                # this is the "root" rule (no extra query params)
                if not params:
                    return rule
                default = rule  # remember this for later if not other rule matches
                continue

            if rule.matches(params):
                return rule

        if default:
            return default

        raise NotFound()


class HttpOperation(NamedTuple):
    operation: OperationModel
    path: str
    method: str
    query: Optional[str]

    @staticmethod
    def from_operation(op: OperationModel) -> "HttpOperation":
        """Useful intermediary representation of the 'http' block of an operation to make code cleaner"""
        uri = op.http.get("requestUri")
        method = op.http.get("method")
        path_query = uri.split("?")
        path = path_query[0]
        query = path_query[1] if len(path_query) > 1 else None

        return HttpOperation(op, path, method, query)


def create_rules_for_ops(ops: List[OperationModel]) -> List[Rule]:
    rules = []

    # first, group all operations by their path and method without possible query strings
    path_index: Dict[(str, str), List[HttpOperation]] = defaultdict(list)
    for op in ops:
        http_op = HttpOperation.from_operation(op)
        path_index[(http_op.path, http_op.method)].append(http_op)

    # now create the werkzeug rules depending on how many operations are in a group
    for (path, method), ops in path_index.items():
        path = path.replace("{", "<path:").replace(
            "}", ">"
        )  # this way we get the path args from werkzeug for free
        # TODO: here we also have to consider path regexes with

        if len(ops) == 1:
            # this is the case for most rules
            op = ops[0]
            rules.append(Rule(path, methods=[method], endpoint=op.operation))
            continue

        rules.append(
            QueryArgsTreeRule(
                path,
                methods=[method],
                query_rules=[QueryArgsRule(op.operation, op.query) for op in ops],
            )
        )

    return rules


def match(matcher: MapAdapter, uri: str, method: str) -> Tuple[OperationModel, Mapping[str, Any]]:
    url = urlparse(uri)
    rule, args = matcher.match(url.path, method=method, return_rule=True)

    if isinstance(rule, QueryArgsTreeRule):
        query_rule = rule.match_query(url.query)
        return query_rule.endpoint, args

    return rule.endpoint, args


def create_service_map(service: ServiceModel) -> Map:
    ops = [service.operation_model(op_name) for op_name in service.operation_names]
    rules = create_rules_for_ops(ops)
    return Map(rules=rules)


class ServiceOpRouter:
    map: Map

    def __init__(self, service: ServiceModel):
        self.map = create_service_map(service)

    def match(self, request: Request) -> Tuple[OperationModel, Mapping[str, Any]]:
        matcher: MapAdapter = self.map.bind(request.host or "localhost")  # FIXME

        rule, args = matcher.match(request.path, method=request.method, return_rule=True)

        if isinstance(rule, QueryArgsTreeRule):
            # could consider using request.args here
            query = request.query_string.decode("utf-8")
            query_rule = rule.match_query(query)
            return query_rule.endpoint, args

        return rule.endpoint, args


if __name__ == "__main__":
    from localstack.aws.spec import load_service

    apigw = load_service("apigateway")

    router = ServiceOpRouter(apigw)

    op, args = router.match(Request("GET", "/restapis/my_id/authorizers"))
    print(op, args)  # OperationModel(name=GetAuthorizers) {'restapi_id': 'my_id'}
    op, args = router.match(Request("GET", "/restapis/my/id/authorizers"))
    print(op, args)  # OperationModel(name=GetAuthorizers) {'restapi_id': 'my/id'}

    op, args = router.match(Request("POST", "/apikeys", query_string="mode=import&foo=bar"))
    print(op, args)  # OperationModel(name=ImportApiKeys) {}

    op, args = router.match(Request("POST", "/apikeys"))
    print(op, args)  # OperationModel(name=CreateApiKey) {}

    op, args = router.match(Request("POST", "/apikeys", query_string="foo=bar"))
    print(op, args)  # OperationModel(name=CreateApiKey) {}
