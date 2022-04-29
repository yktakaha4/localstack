import json
import os
from collections import defaultdict
from typing import Tuple

from botocore.model import OperationModel

from localstack.aws.spec import load_service

target_dir = "/home/thomas/workspace/localstack/localstack/target"


def load_session(session_id):
    ndjson = os.path.join(target_dir, "api-requests", f"calls-{session_id}.ndjson")

    with open(ndjson, "r") as fd:
        for line in fd:
            yield json.loads(line)


def calculate_operation_coverage(service, operation_params) -> Tuple[int, int]:
    service_model = load_service(service)

    total_ops = len(service_model.operation_names)
    covered_ops = len(operation_params.keys())

    return total_ops, covered_ops


def calculate_parameter_coverage(service, operation, params) -> Tuple[int, int]:
    service_model = load_service(service)
    operation_model: OperationModel = service_model.operation_model(operation)

    input_shape = operation_model.input_shape

    if not input_shape:
        return 1, 1

    total_params = len(input_shape.members)
    if not total_params:
        return 1, 1

    covered_params = len(params)
    return total_params, covered_params


def main():
    # recorded = load_session(session_id="a96231f3-1faa-4959-9ecd-29791b6b2d72")
    recorded = load_session(session_id="ca733708-45ce-415e-8535-e733a8b4b3c9")

    service_operation_params = defaultdict(lambda: defaultdict(set))
    for call in recorded:
        service = call["service"]
        operation = call["operation"]
        params = call["params"].keys()  # TODO: tree
        service_operation_params[service][operation].update(params)

    print("service operation coverage")
    print("service,coverage,covered,missed")
    for service, operation_params in service_operation_params.items():
        total, covered = calculate_operation_coverage(service, operation_params)
        print(f"{service},{covered/total*100:.0f},{covered},{total - covered}")

    print("----")
    print("service operation coverage")
    for service, operation_params in service_operation_params.items():
        total, covered = calculate_operation_coverage(service, operation_params)
        print(
            f"{service}: {covered/total*100:.0f}% (covered: {covered}, missed: {total - covered})"
        )

        for operation, params in operation_params.items():
            total, covered = calculate_parameter_coverage(service, operation, params)
            print(
                f"  - {operation:30s}: {covered / total * 100:3.0f}% (covered: {covered}, missed: {total - covered})"
            )


if __name__ == "__main__":
    main()
