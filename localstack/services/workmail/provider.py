from localstack.aws.api import RequestContext
from localstack.aws.api.workmail import WorkmailApi, OrganizationId, WorkMailIdentifier, \
    UserName, String, Password, CreateUserResponse, EmailAddress, \
    RegisterToWorkMailResponse, DeregisterFromWorkMailResponse, DeleteUserResponse, NextToken, MaxResults, \
    ListUsersResponse
from localstack.services.plugins import ServiceLifecycleHook


class WorkmailProvider(WorkmailApi, ServiceLifecycleHook):
    def register_to_work_mail(self, context: RequestContext, organization_id: OrganizationId,
                              entity_id: WorkMailIdentifier, email: EmailAddress) -> RegisterToWorkMailResponse:
        pass

    def deregister_from_work_mail(self, context: RequestContext, organization_id: OrganizationId,
                                  entity_id: WorkMailIdentifier) -> DeregisterFromWorkMailResponse:
        pass

    def create_user(self, context: RequestContext, organization_id: OrganizationId, name: UserName,
                    display_name: String, password: Password) -> CreateUserResponse:
        pass

    def delete_user(self, context: RequestContext, organization_id: OrganizationId,
                    user_id: WorkMailIdentifier) -> DeleteUserResponse:
        pass

    def list_users(self, context: RequestContext, organization_id: OrganizationId, next_token: NextToken = None,
                   max_results: MaxResults = None) -> ListUsersResponse:
        pass
