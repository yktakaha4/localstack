from localstack.aws.api.cloudformation import *
from localstack.services.generic_proxy import RegionBackend
from localstack.services.plugins import ServiceLifecycleHook

# TODO: set up state

class CloudformationBackend(RegionBackend):
    pass


class CfnProvider(CloudformationApi, ServiceLifecycleHook):

    def create_stack(
            self,
            context: RequestContext,
            stack_name: StackName,
            template_body: TemplateBody = None,
            template_url: TemplateURL = None,
            parameters: Parameters = None,
            disable_rollback: DisableRollback = None,  # TODO
            rollback_configuration: RollbackConfiguration = None,  # TODO
            timeout_in_minutes: TimeoutMinutes = None,  # TODO
            notification_arns: NotificationARNs = None,  # TODO
            capabilities: Capabilities = None,
            resource_types: ResourceTypes = None,  # TODO
            role_arn: RoleARN = None,  # TODO
            on_failure: OnFailure = None,  # TODO
            stack_policy_body: StackPolicyBody = None,  # TODO
            stack_policy_url: StackPolicyURL = None,  # TODO
            tags: Tags = None,  # TODO
            client_request_token: ClientRequestToken = None,  # TODO: what does this do?
            enable_termination_protection: EnableTerminationProtection = None,  # TODO
    ) -> CreateStackOutput:
        return {}

    def describe_stacks(
        self,
        context: RequestContext,
        stack_name: StackName = None,
        next_token: NextToken = None,
    ) -> DescribeStacksOutput:
        return {}

    def delete_stack(
            self,
            context: RequestContext,
            stack_name: StackName,
            retain_resources: RetainResources = None,
            role_arn: RoleARN = None,
            client_request_token: ClientRequestToken = None,
    ) -> None:
        return {}

    def create_change_set(
            self,
            context: RequestContext,
            stack_name: StackNameOrId,
            change_set_name: ChangeSetName,
            template_body: TemplateBody = None,
            template_url: TemplateURL = None,
            use_previous_template: UsePreviousTemplate = None,
            parameters: Parameters = None,
            capabilities: Capabilities = None,
            resource_types: ResourceTypes = None,
            role_arn: RoleARN = None,
            rollback_configuration: RollbackConfiguration = None,
            notification_arns: NotificationARNs = None,
            tags: Tags = None,
            client_token: ClientToken = None,
            description: Description = None,
            change_set_type: ChangeSetType = None,
            resources_to_import: ResourcesToImport = None,
            include_nested_stacks: IncludeNestedStacks = None,
    ) -> CreateChangeSetOutput:
        return {}

    def describe_change_set(
        self,
        context: RequestContext,
        change_set_name: ChangeSetNameOrId,
        stack_name: StackNameOrId = None,
        next_token: NextToken = None,
    ) -> DescribeChangeSetOutput:
        pass

    def execute_change_set(
            self,
            context: RequestContext,
            change_set_name: ChangeSetNameOrId,
            stack_name: StackNameOrId = None,
            client_request_token: ClientRequestToken = None,
            disable_rollback: DisableRollback = None,
    ) -> ExecuteChangeSetOutput:
        return {}

    def delete_change_set(
            self,
            context: RequestContext,
            change_set_name: ChangeSetNameOrId,
            stack_name: StackNameOrId = None,
    ) -> DeleteChangeSetOutput:
        return {}


    def describe_stack_resources(
        self,
        context: RequestContext,
        stack_name: StackName = None,
        logical_resource_id: LogicalResourceId = None,
        physical_resource_id: PhysicalResourceId = None,
    ) -> DescribeStackResourcesOutput:
        return {}


    def describe_stack_resource(
        self,
        context: RequestContext,
        stack_name: StackName,
        logical_resource_id: LogicalResourceId,
    ) -> DescribeStackResourceOutput:
        return {}

