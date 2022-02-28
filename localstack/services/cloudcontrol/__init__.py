from localstack.aws.api import RequestContext
from localstack.aws.api.cloudcontrol import CloudcontrolApi, TypeName, Identifier, PatchDocument, TypeVersionId, \
    RoleArn, ClientToken, UpdateResourceOutput, HandlerNextToken, MaxResults, Properties, ListResourcesOutput, \
    NextToken, ResourceRequestStatusFilter, ListResourceRequestsOutput, RequestToken, GetResourceRequestStatusOutput, \
    GetResourceOutput, DeleteResourceOutput, CreateResourceOutput, CancelResourceRequestOutput
from localstack.services.generic_proxy import RegionBackend


class CloudControlBackend(RegionBackend):
    """ only used for tracking ongoing progress of internal operations """
    pass


class CloudControlProvider(CloudcontrolApi):

    # CRUD-L

    def create_resource(self, context: RequestContext, type_name: TypeName, desired_state: Properties,
                        type_version_id: TypeVersionId = None, role_arn: RoleArn = None,
                        client_token: ClientToken = None) -> CreateResourceOutput:
        pass

    def get_resource(self, context: RequestContext, type_name: TypeName, identifier: Identifier,
                     type_version_id: TypeVersionId = None, role_arn: RoleArn = None) -> GetResourceOutput:
        pass

    def update_resource(self, context: RequestContext, type_name: TypeName, identifier: Identifier,
                        patch_document: PatchDocument, type_version_id: TypeVersionId = None, role_arn: RoleArn = None,
                        client_token: ClientToken = None) -> UpdateResourceOutput:
        pass

    def delete_resource(self, context: RequestContext, type_name: TypeName, identifier: Identifier,
                        type_version_id: TypeVersionId = None, role_arn: RoleArn = None,
                        client_token: ClientToken = None) -> DeleteResourceOutput:
        pass

    def list_resources(self, context: RequestContext, type_name: TypeName, type_version_id: TypeVersionId = None,
                       role_arn: RoleArn = None, next_token: HandlerNextToken = None, max_results: MaxResults = None,
                       resource_model: Properties = None) -> ListResourcesOutput:
        pass



    # resource request operations
    def get_resource_request_status(self, context: RequestContext,
                                    request_token: RequestToken) -> GetResourceRequestStatusOutput:
        pass

    def list_resource_requests(self, context: RequestContext, max_results: MaxResults = None,
                               next_token: NextToken = None,
                               resource_request_status_filter: ResourceRequestStatusFilter = None) -> ListResourceRequestsOutput:
        pass

    def cancel_resource_request(self, context: RequestContext,
                                request_token: RequestToken) -> CancelResourceRequestOutput:
        pass
