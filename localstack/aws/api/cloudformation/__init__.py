import sys
from typing import Dict, List, Optional
from datetime import datetime

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from localstack.aws.api import handler, RequestContext, ServiceException, ServiceRequest

AcceptTermsAndConditions = bool
Account = str
AccountGateStatusReason = str
AccountsUrl = str
AllowedValue = str
Arn = str
AutoDeploymentNullable = bool
AutoUpdate = bool
BoxedInteger = int
BoxedMaxResults = int
CapabilitiesReason = str
CausingEntity = str
ChangeSetId = str
ChangeSetName = str
ChangeSetNameOrId = str
ChangeSetStatusReason = str
ClientRequestToken = str
ClientToken = str
ConfigurationSchema = str
ConnectionArn = str
Description = str
DisableRollback = bool
DriftedStackInstancesCount = int
EnableTerminationProtection = bool
ErrorCode = str
ErrorMessage = str
EventId = str
ExecutionRoleName = str
ExportName = str
ExportValue = str
FailedStackInstancesCount = int
FailureToleranceCount = int
FailureTolerancePercentage = int
HookInvocationCount = int
HookStatusReason = str
HookTargetTypeName = str
HookType = str
HookTypeConfigurationVersionId = str
HookTypeName = str
HookTypeVersionId = str
InProgressStackInstancesCount = int
InSyncStackInstancesCount = int
IncludeNestedStacks = bool
IsActivated = bool
IsDefaultConfiguration = bool
IsDefaultVersion = bool
Key = str
LimitName = str
LimitValue = int
LogGroupName = str
LogicalIdHierarchy = str
LogicalResourceId = str
ManagedExecutionNullable = bool
MaxConcurrentCount = int
MaxConcurrentPercentage = int
MaxResults = int
Metadata = str
MonitoringTimeInMinutes = int
NextToken = str
NoEcho = bool
NotificationARN = str
OptionalSecureUrl = str
OrganizationalUnitId = str
OutputKey = str
OutputValue = str
ParameterKey = str
ParameterType = str
ParameterValue = str
PhysicalResourceId = str
PrivateTypeArn = str
Properties = str
PropertyName = str
PropertyPath = str
PropertyValue = str
PublicVersionNumber = str
PublisherId = str
PublisherName = str
PublisherProfile = str
Reason = str
Region = str
RegistrationToken = str
RequestToken = str
ResourceIdentifierPropertyKey = str
ResourceIdentifierPropertyValue = str
ResourceModel = str
ResourceProperties = str
ResourceSignalUniqueId = str
ResourceStatusReason = str
ResourceToSkip = str
ResourceType = str
RetainStacks = bool
RetainStacksNullable = bool
RetainStacksOnAccountRemovalNullable = bool
RoleARN = str
RoleArn = str
S3Bucket = str
S3Url = str
StackDriftDetectionId = str
StackDriftDetectionStatusReason = str
StackId = str
StackIdsUrl = str
StackInstanceFilterValues = str
StackName = str
StackNameOrId = str
StackPolicyBody = str
StackPolicyDuringUpdateBody = str
StackPolicyDuringUpdateURL = str
StackPolicyURL = str
StackSetARN = str
StackSetId = str
StackSetName = str
StackSetNameOrId = str
StackStatusReason = str
StatusMessage = str
SupportedMajorVersion = int
TagKey = str
TagValue = str
TemplateBody = str
TemplateDescription = str
TemplateURL = str
ThirdPartyTypeArn = str
TimeoutMinutes = int
TotalStackInstancesCount = int
TransformName = str
Type = str
TypeArn = str
TypeConfiguration = str
TypeConfigurationAlias = str
TypeConfigurationArn = str
TypeHierarchy = str
TypeName = str
TypeNamePrefix = str
TypeSchema = str
TypeTestsStatusDescription = str
TypeVersionId = str
Url = str
UsePreviousTemplate = bool
UsePreviousValue = bool
Value = str
Version = str


class AccountGateStatus(str):
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


class CallAs(str):
    SELF = "SELF"
    DELEGATED_ADMIN = "DELEGATED_ADMIN"


class Capability(str):
    CAPABILITY_IAM = "CAPABILITY_IAM"
    CAPABILITY_NAMED_IAM = "CAPABILITY_NAMED_IAM"
    CAPABILITY_AUTO_EXPAND = "CAPABILITY_AUTO_EXPAND"


class Category(str):
    REGISTERED = "REGISTERED"
    ACTIVATED = "ACTIVATED"
    THIRD_PARTY = "THIRD_PARTY"
    AWS_TYPES = "AWS_TYPES"


class ChangeAction(str):
    Add = "Add"
    Modify = "Modify"
    Remove = "Remove"
    Import = "Import"
    Dynamic = "Dynamic"


class ChangeSetHooksStatus(str):
    PLANNING = "PLANNING"
    PLANNED = "PLANNED"
    UNAVAILABLE = "UNAVAILABLE"


class ChangeSetStatus(str):
    CREATE_PENDING = "CREATE_PENDING"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    DELETE_PENDING = "DELETE_PENDING"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_FAILED = "DELETE_FAILED"
    FAILED = "FAILED"


class ChangeSetType(str):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    IMPORT = "IMPORT"


class ChangeSource(str):
    ResourceReference = "ResourceReference"
    ParameterReference = "ParameterReference"
    ResourceAttribute = "ResourceAttribute"
    DirectModification = "DirectModification"
    Automatic = "Automatic"


class ChangeType(str):
    Resource = "Resource"


class DeprecatedStatus(str):
    LIVE = "LIVE"
    DEPRECATED = "DEPRECATED"


class DifferenceType(str):
    ADD = "ADD"
    REMOVE = "REMOVE"
    NOT_EQUAL = "NOT_EQUAL"


class EvaluationType(str):
    Static = "Static"
    Dynamic = "Dynamic"


class ExecutionStatus(str):
    UNAVAILABLE = "UNAVAILABLE"
    AVAILABLE = "AVAILABLE"
    EXECUTE_IN_PROGRESS = "EXECUTE_IN_PROGRESS"
    EXECUTE_COMPLETE = "EXECUTE_COMPLETE"
    EXECUTE_FAILED = "EXECUTE_FAILED"
    OBSOLETE = "OBSOLETE"


class HandlerErrorCode(str):
    NotUpdatable = "NotUpdatable"
    InvalidRequest = "InvalidRequest"
    AccessDenied = "AccessDenied"
    InvalidCredentials = "InvalidCredentials"
    AlreadyExists = "AlreadyExists"
    NotFound = "NotFound"
    ResourceConflict = "ResourceConflict"
    Throttling = "Throttling"
    ServiceLimitExceeded = "ServiceLimitExceeded"
    NotStabilized = "NotStabilized"
    GeneralServiceException = "GeneralServiceException"
    ServiceInternalError = "ServiceInternalError"
    NetworkFailure = "NetworkFailure"
    InternalFailure = "InternalFailure"
    InvalidTypeConfiguration = "InvalidTypeConfiguration"
    HandlerInternalFailure = "HandlerInternalFailure"
    NonCompliant = "NonCompliant"
    Unknown = "Unknown"


class HookFailureMode(str):
    FAIL = "FAIL"
    WARN = "WARN"


class HookInvocationPoint(str):
    PRE_PROVISION = "PRE_PROVISION"


class HookStatus(str):
    HOOK_IN_PROGRESS = "HOOK_IN_PROGRESS"
    HOOK_COMPLETE_SUCCEEDED = "HOOK_COMPLETE_SUCCEEDED"
    HOOK_COMPLETE_FAILED = "HOOK_COMPLETE_FAILED"
    HOOK_FAILED = "HOOK_FAILED"


class HookTargetType(str):
    RESOURCE = "RESOURCE"


class IdentityProvider(str):
    AWS_Marketplace = "AWS_Marketplace"
    GitHub = "GitHub"
    Bitbucket = "Bitbucket"


class OnFailure(str):
    DO_NOTHING = "DO_NOTHING"
    ROLLBACK = "ROLLBACK"
    DELETE = "DELETE"


class OperationStatus(str):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class PermissionModels(str):
    SERVICE_MANAGED = "SERVICE_MANAGED"
    SELF_MANAGED = "SELF_MANAGED"


class ProvisioningType(str):
    NON_PROVISIONABLE = "NON_PROVISIONABLE"
    IMMUTABLE = "IMMUTABLE"
    FULLY_MUTABLE = "FULLY_MUTABLE"


class PublisherStatus(str):
    VERIFIED = "VERIFIED"
    UNVERIFIED = "UNVERIFIED"


class RegionConcurrencyType(str):
    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL = "PARALLEL"


class RegistrationStatus(str):
    COMPLETE = "COMPLETE"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"


class RegistryType(str):
    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"


class Replacement(str):
    True_ = "True"
    False_ = "False"
    Conditional = "Conditional"


class RequiresRecreation(str):
    Never = "Never"
    Conditionally = "Conditionally"
    Always = "Always"


class ResourceAttribute(str):
    Properties = "Properties"
    Metadata = "Metadata"
    CreationPolicy = "CreationPolicy"
    UpdatePolicy = "UpdatePolicy"
    DeletionPolicy = "DeletionPolicy"
    Tags = "Tags"


class ResourceSignalStatus(str):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class ResourceStatus(str):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_SKIPPED = "DELETE_SKIPPED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    IMPORT_FAILED = "IMPORT_FAILED"
    IMPORT_COMPLETE = "IMPORT_COMPLETE"
    IMPORT_IN_PROGRESS = "IMPORT_IN_PROGRESS"
    IMPORT_ROLLBACK_IN_PROGRESS = "IMPORT_ROLLBACK_IN_PROGRESS"
    IMPORT_ROLLBACK_FAILED = "IMPORT_ROLLBACK_FAILED"
    IMPORT_ROLLBACK_COMPLETE = "IMPORT_ROLLBACK_COMPLETE"
    UPDATE_ROLLBACK_IN_PROGRESS = "UPDATE_ROLLBACK_IN_PROGRESS"
    UPDATE_ROLLBACK_COMPLETE = "UPDATE_ROLLBACK_COMPLETE"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"


class StackDriftDetectionStatus(str):
    DETECTION_IN_PROGRESS = "DETECTION_IN_PROGRESS"
    DETECTION_FAILED = "DETECTION_FAILED"
    DETECTION_COMPLETE = "DETECTION_COMPLETE"


class StackDriftStatus(str):
    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"
    UNKNOWN = "UNKNOWN"
    NOT_CHECKED = "NOT_CHECKED"


class StackInstanceDetailedStatus(str):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    INOPERABLE = "INOPERABLE"


class StackInstanceFilterName(str):
    DETAILED_STATUS = "DETAILED_STATUS"


class StackInstanceStatus(str):
    CURRENT = "CURRENT"
    OUTDATED = "OUTDATED"
    INOPERABLE = "INOPERABLE"


class StackResourceDriftStatus(str):
    IN_SYNC = "IN_SYNC"
    MODIFIED = "MODIFIED"
    DELETED = "DELETED"
    NOT_CHECKED = "NOT_CHECKED"


class StackSetDriftDetectionStatus(str):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    IN_PROGRESS = "IN_PROGRESS"
    STOPPED = "STOPPED"


class StackSetDriftStatus(str):
    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"
    NOT_CHECKED = "NOT_CHECKED"


class StackSetOperationAction(str):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    DETECT_DRIFT = "DETECT_DRIFT"


class StackSetOperationResultStatus(str):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class StackSetOperationStatus(str):
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    QUEUED = "QUEUED"


class StackSetStatus(str):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"


class StackStatus(str):
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_COMPLETE = "CREATE_COMPLETE"
    ROLLBACK_IN_PROGRESS = "ROLLBACK_IN_PROGRESS"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_COMPLETE_CLEANUP_IN_PROGRESS = "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPDATE_ROLLBACK_IN_PROGRESS = "UPDATE_ROLLBACK_IN_PROGRESS"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS = (
        "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS"
    )
    UPDATE_ROLLBACK_COMPLETE = "UPDATE_ROLLBACK_COMPLETE"
    REVIEW_IN_PROGRESS = "REVIEW_IN_PROGRESS"
    IMPORT_IN_PROGRESS = "IMPORT_IN_PROGRESS"
    IMPORT_COMPLETE = "IMPORT_COMPLETE"
    IMPORT_ROLLBACK_IN_PROGRESS = "IMPORT_ROLLBACK_IN_PROGRESS"
    IMPORT_ROLLBACK_FAILED = "IMPORT_ROLLBACK_FAILED"
    IMPORT_ROLLBACK_COMPLETE = "IMPORT_ROLLBACK_COMPLETE"


class TemplateStage(str):
    Original = "Original"
    Processed = "Processed"


class ThirdPartyType(str):
    RESOURCE = "RESOURCE"
    MODULE = "MODULE"
    HOOK = "HOOK"


class TypeTestsStatus(str):
    PASSED = "PASSED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_TESTED = "NOT_TESTED"


class VersionBump(str):
    MAJOR = "MAJOR"
    MINOR = "MINOR"


class Visibility(str):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class AlreadyExistsException(ServiceException):
    """The resource with the name requested already exists."""

    pass


class CFNRegistryException(ServiceException):
    """An error occurred during a CloudFormation registry operation."""

    Message: Optional[ErrorMessage]


class ChangeSetNotFoundException(ServiceException):
    """The specified change set name or ID doesn't exit. To view valid change
    sets for a stack, use the ``ListChangeSets`` operation.
    """

    pass


class CreatedButModifiedException(ServiceException):
    """The specified resource exists, but has been changed."""

    pass


class InsufficientCapabilitiesException(ServiceException):
    """The template contains resources with capabilities that weren't specified
    in the Capabilities parameter.
    """

    pass


class InvalidChangeSetStatusException(ServiceException):
    """The specified change set can't be used to update the stack. For example,
    the change set status might be ``CREATE_IN_PROGRESS``, or the stack
    status might be ``UPDATE_IN_PROGRESS``.
    """

    pass


class InvalidOperationException(ServiceException):
    """The specified operation isn't valid."""

    pass


class InvalidStateTransitionException(ServiceException):
    """Error reserved for use by the `CloudFormation
    CLI <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html>`__.
    CloudFormation doesn't return this error to users.
    """

    pass


class LimitExceededException(ServiceException):
    """The quota for the resource has already been reached.

    For information on resource and stack limitations, see `CloudFormation
    quotas <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
    in the *CloudFormation User Guide*.
    """

    pass


class NameAlreadyExistsException(ServiceException):
    """The specified name is already in use."""

    pass


class OperationIdAlreadyExistsException(ServiceException):
    """The specified operation ID already exists."""

    pass


class OperationInProgressException(ServiceException):
    """Another operation is currently in progress for this stack set. Only one
    operation can be performed for a stack set at a given time.
    """

    pass


class OperationNotFoundException(ServiceException):
    """The specified ID refers to an operation that doesn't exist."""

    pass


class OperationStatusCheckFailedException(ServiceException):
    """Error reserved for use by the `CloudFormation
    CLI <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html>`__.
    CloudFormation doesn't return this error to users.
    """

    pass


class StackInstanceNotFoundException(ServiceException):
    """The specified stack instance doesn't exist."""

    pass


class StackNotFoundException(ServiceException):
    """The specified stack ARN doesn't exist or stack doesn't exist
    corresponding to the ARN in input.
    """

    pass


class StackSetNotEmptyException(ServiceException):
    """You can't yet delete this stack set, because it still contains one or
    more stack instances. Delete all stack instances from the stack set
    before deleting the stack set.
    """

    pass


class StackSetNotFoundException(ServiceException):
    """The specified stack set doesn't exist."""

    pass


class StaleRequestException(ServiceException):
    """Another operation has been performed on this stack set since the
    specified operation was performed.
    """

    pass


class TokenAlreadyExistsException(ServiceException):
    """A client request token already exists."""

    pass


class TypeConfigurationNotFoundException(ServiceException):
    """The specified extension configuration can't be found."""

    pass


class TypeNotFoundException(ServiceException):
    """The specified extension doesn't exist in the CloudFormation registry."""

    pass


class AccountGateResult(TypedDict, total=False):
    """Structure that contains the results of the account gate function which
    CloudFormation invokes, if present, before proceeding with a stack set
    operation in an account and Region.

    For each account and Region, CloudFormation lets you specify a Lambda
    function that encapsulates any requirements that must be met before
    CloudFormation can proceed with a stack set operation in that account
    and Region. CloudFormation invokes the function each time a stack set
    operation is requested for that account and Region; if the function
    returns ``FAILED``, CloudFormation cancels the operation in that account
    and Region, and sets the stack set operation result status for that
    account and Region to ``FAILED``.

    For more information, see `Configuring a target account
    gate <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-account-gating.html>`__.
    """

    Status: Optional[AccountGateStatus]
    StatusReason: Optional[AccountGateStatusReason]


class AccountLimit(TypedDict, total=False):
    """The AccountLimit data type.

    CloudFormation has the following limits per account:

    -  Number of concurrent resources

    -  Number of stacks

    -  Number of stack outputs

    For more information about these account limits, and other
    CloudFormation limits, see `CloudFormation
    quotas <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
    in the *CloudFormation User Guide*.
    """

    Name: Optional[LimitName]
    Value: Optional[LimitValue]


AccountLimitList = List[AccountLimit]
AccountList = List[Account]
MajorVersion = int


class LoggingConfig(TypedDict, total=False):
    """Contains logging configuration information for an extension."""

    LogRoleArn: RoleArn
    LogGroupName: LogGroupName


class ActivateTypeInput(ServiceRequest):
    Type: Optional[ThirdPartyType]
    PublicTypeArn: Optional[ThirdPartyTypeArn]
    PublisherId: Optional[PublisherId]
    TypeName: Optional[TypeName]
    TypeNameAlias: Optional[TypeName]
    AutoUpdate: Optional[AutoUpdate]
    LoggingConfig: Optional[LoggingConfig]
    ExecutionRoleArn: Optional[RoleArn]
    VersionBump: Optional[VersionBump]
    MajorVersion: Optional[MajorVersion]


class ActivateTypeOutput(TypedDict, total=False):
    Arn: Optional[PrivateTypeArn]


AllowedValues = List[AllowedValue]


class AutoDeployment(TypedDict, total=False):
    """[Service-managed permissions] Describes whether StackSets automatically
    deploys to Organizations accounts that are added to a target
    organization or organizational unit (OU).
    """

    Enabled: Optional[AutoDeploymentNullable]
    RetainStacksOnAccountRemoval: Optional[RetainStacksOnAccountRemovalNullable]


class TypeConfigurationIdentifier(TypedDict, total=False):
    """Identifying information for the configuration of a CloudFormation
    extension.
    """

    TypeArn: Optional[TypeArn]
    TypeConfigurationAlias: Optional[TypeConfigurationAlias]
    TypeConfigurationArn: Optional[TypeConfigurationArn]
    Type: Optional[ThirdPartyType]
    TypeName: Optional[TypeName]


class BatchDescribeTypeConfigurationsError(TypedDict, total=False):
    """Detailed information concerning an error generated during the setting of
    configuration data for a CloudFormation extension.
    """

    ErrorCode: Optional[ErrorCode]
    ErrorMessage: Optional[ErrorMessage]
    TypeConfigurationIdentifier: Optional[TypeConfigurationIdentifier]


BatchDescribeTypeConfigurationsErrors = List[BatchDescribeTypeConfigurationsError]
TypeConfigurationIdentifiers = List[TypeConfigurationIdentifier]


class BatchDescribeTypeConfigurationsInput(ServiceRequest):
    TypeConfigurationIdentifiers: TypeConfigurationIdentifiers


Timestamp = datetime


class TypeConfigurationDetails(TypedDict, total=False):
    """Detailed information concerning the specification of a CloudFormation
    extension in a given account and region.

    For more information, see `Configuring extensions at the account
    level <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration>`__
    in the *CloudFormation User Guide*.
    """

    Arn: Optional[TypeConfigurationArn]
    Alias: Optional[TypeConfigurationAlias]
    Configuration: Optional[TypeConfiguration]
    LastUpdated: Optional[Timestamp]
    TypeArn: Optional[TypeArn]
    TypeName: Optional[TypeName]
    IsDefaultConfiguration: Optional[IsDefaultConfiguration]


TypeConfigurationDetailsList = List[TypeConfigurationDetails]
UnprocessedTypeConfigurations = List[TypeConfigurationIdentifier]


class BatchDescribeTypeConfigurationsOutput(TypedDict, total=False):
    Errors: Optional[BatchDescribeTypeConfigurationsErrors]
    UnprocessedTypeConfigurations: Optional[UnprocessedTypeConfigurations]
    TypeConfigurations: Optional[TypeConfigurationDetailsList]


class CancelUpdateStackInput(ServiceRequest):
    """The input for the CancelUpdateStack action."""

    StackName: StackName
    ClientRequestToken: Optional[ClientRequestToken]


Capabilities = List[Capability]


class ModuleInfo(TypedDict, total=False):
    """Contains information about the module from which the resource was
    created, if the resource was created from a module included in the stack
    template.

    For more information on modules, see `Using modules to encapsulate and
    reuse resource
    configurations <AWSCloudFormation/latest/UserGuide/modules.html>`__ in
    the *CloudFormation User Guide*.
    """

    TypeHierarchy: Optional[TypeHierarchy]
    LogicalIdHierarchy: Optional[LogicalIdHierarchy]


class ResourceTargetDefinition(TypedDict, total=False):
    """The field that CloudFormation will change, such as the name of a
    resource's property, and whether the resource will be recreated.
    """

    Attribute: Optional[ResourceAttribute]
    Name: Optional[PropertyName]
    RequiresRecreation: Optional[RequiresRecreation]


class ResourceChangeDetail(TypedDict, total=False):
    """For a resource with ``Modify`` as the action, the ``ResourceChange``
    structure describes the changes CloudFormation will make to that
    resource.
    """

    Target: Optional[ResourceTargetDefinition]
    Evaluation: Optional[EvaluationType]
    ChangeSource: Optional[ChangeSource]
    CausingEntity: Optional[CausingEntity]


ResourceChangeDetails = List[ResourceChangeDetail]
Scope = List[ResourceAttribute]


class ResourceChange(TypedDict, total=False):
    """The ``ResourceChange`` structure describes the resource and the action
    that CloudFormation will perform on it if you execute this change set.
    """

    Action: Optional[ChangeAction]
    LogicalResourceId: Optional[LogicalResourceId]
    PhysicalResourceId: Optional[PhysicalResourceId]
    ResourceType: Optional[ResourceType]
    Replacement: Optional[Replacement]
    Scope: Optional[Scope]
    Details: Optional[ResourceChangeDetails]
    ChangeSetId: Optional[ChangeSetId]
    ModuleInfo: Optional[ModuleInfo]


class Change(TypedDict, total=False):
    """The ``Change`` structure describes the changes CloudFormation will
    perform if you execute the change set.
    """

    Type: Optional[ChangeType]
    HookInvocationCount: Optional[HookInvocationCount]
    ResourceChange: Optional[ResourceChange]


class ChangeSetHookResourceTargetDetails(TypedDict, total=False):
    """Specifies ``RESOURCE`` type target details for activated hooks."""

    LogicalResourceId: Optional[LogicalResourceId]
    ResourceType: Optional[HookTargetTypeName]
    ResourceAction: Optional[ChangeAction]


class ChangeSetHookTargetDetails(TypedDict, total=False):
    """Specifies target details for an activated hook."""

    TargetType: Optional[HookTargetType]
    ResourceTargetDetails: Optional[ChangeSetHookResourceTargetDetails]


class ChangeSetHook(TypedDict, total=False):
    """Specifies the resource, the hook, and the hook version to be invoked."""

    InvocationPoint: Optional[HookInvocationPoint]
    FailureMode: Optional[HookFailureMode]
    TypeName: Optional[HookTypeName]
    TypeVersionId: Optional[HookTypeVersionId]
    TypeConfigurationVersionId: Optional[HookTypeConfigurationVersionId]
    TargetDetails: Optional[ChangeSetHookTargetDetails]


ChangeSetHooks = List[ChangeSetHook]
CreationTime = datetime


class ChangeSetSummary(TypedDict, total=False):
    """The ``ChangeSetSummary`` structure describes a change set, its status,
    and the stack with which it's associated.
    """

    StackId: Optional[StackId]
    StackName: Optional[StackName]
    ChangeSetId: Optional[ChangeSetId]
    ChangeSetName: Optional[ChangeSetName]
    ExecutionStatus: Optional[ExecutionStatus]
    Status: Optional[ChangeSetStatus]
    StatusReason: Optional[ChangeSetStatusReason]
    CreationTime: Optional[CreationTime]
    Description: Optional[Description]
    IncludeNestedStacks: Optional[IncludeNestedStacks]
    ParentChangeSetId: Optional[ChangeSetId]
    RootChangeSetId: Optional[ChangeSetId]


ChangeSetSummaries = List[ChangeSetSummary]
Changes = List[Change]
ResourcesToSkip = List[ResourceToSkip]


class ContinueUpdateRollbackInput(ServiceRequest):
    """The input for the ContinueUpdateRollback action."""

    StackName: StackNameOrId
    RoleARN: Optional[RoleARN]
    ResourcesToSkip: Optional[ResourcesToSkip]
    ClientRequestToken: Optional[ClientRequestToken]


class ContinueUpdateRollbackOutput(TypedDict, total=False):
    """The output for a ContinueUpdateRollback operation."""

    pass


ResourceIdentifierProperties = Dict[
    ResourceIdentifierPropertyKey, ResourceIdentifierPropertyValue
]


class ResourceToImport(TypedDict, total=False):
    """Describes the target resource of an import operation."""

    ResourceType: ResourceType
    LogicalResourceId: LogicalResourceId
    ResourceIdentifier: ResourceIdentifierProperties


ResourcesToImport = List[ResourceToImport]


class Tag(TypedDict, total=False):
    """The Tag type enables you to specify a key-value pair that can be used to
    store information about an CloudFormation stack.
    """

    Key: TagKey
    Value: TagValue


Tags = List[Tag]
NotificationARNs = List[NotificationARN]


class RollbackTrigger(TypedDict, total=False):
    """A rollback trigger CloudFormation monitors during creation and updating
    of stacks. If any of the alarms you specify goes to ALARM state during
    the stack operation or within the specified monitoring period
    afterwards, CloudFormation rolls back the entire stack operation.
    """

    Arn: Arn
    Type: Type


RollbackTriggers = List[RollbackTrigger]


class RollbackConfiguration(TypedDict, total=False):
    """Structure containing the rollback triggers for CloudFormation to monitor
    during stack creation and updating operations, and for the specified
    monitoring period afterwards.

    Rollback triggers enable you to have CloudFormation monitor the state of
    your application during stack creation and updating, and to roll back
    that operation if the application breaches the threshold of any of the
    alarms you've specified. For more information, see `Monitor and Roll
    Back Stack
    Operations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-rollback-triggers.html>`__.
    """

    RollbackTriggers: Optional[RollbackTriggers]
    MonitoringTimeInMinutes: Optional[MonitoringTimeInMinutes]


ResourceTypes = List[ResourceType]


class Parameter(TypedDict, total=False):
    """The Parameter data type."""

    ParameterKey: Optional[ParameterKey]
    ParameterValue: Optional[ParameterValue]
    UsePreviousValue: Optional[UsePreviousValue]
    ResolvedValue: Optional[ParameterValue]


Parameters = List[Parameter]


class CreateChangeSetInput(ServiceRequest):
    """The input for the CreateChangeSet action."""

    StackName: StackNameOrId
    TemplateBody: Optional[TemplateBody]
    TemplateURL: Optional[TemplateURL]
    UsePreviousTemplate: Optional[UsePreviousTemplate]
    Parameters: Optional[Parameters]
    Capabilities: Optional[Capabilities]
    ResourceTypes: Optional[ResourceTypes]
    RoleARN: Optional[RoleARN]
    RollbackConfiguration: Optional[RollbackConfiguration]
    NotificationARNs: Optional[NotificationARNs]
    Tags: Optional[Tags]
    ChangeSetName: ChangeSetName
    ClientToken: Optional[ClientToken]
    Description: Optional[Description]
    ChangeSetType: Optional[ChangeSetType]
    ResourcesToImport: Optional[ResourcesToImport]
    IncludeNestedStacks: Optional[IncludeNestedStacks]


class CreateChangeSetOutput(TypedDict, total=False):
    """The output for the CreateChangeSet action."""

    Id: Optional[ChangeSetId]
    StackId: Optional[StackId]


class CreateStackInput(ServiceRequest):
    """The input for CreateStack action."""

    StackName: StackName
    TemplateBody: Optional[TemplateBody]
    TemplateURL: Optional[TemplateURL]
    Parameters: Optional[Parameters]
    DisableRollback: Optional[DisableRollback]
    RollbackConfiguration: Optional[RollbackConfiguration]
    TimeoutInMinutes: Optional[TimeoutMinutes]
    NotificationARNs: Optional[NotificationARNs]
    Capabilities: Optional[Capabilities]
    ResourceTypes: Optional[ResourceTypes]
    RoleARN: Optional[RoleARN]
    OnFailure: Optional[OnFailure]
    StackPolicyBody: Optional[StackPolicyBody]
    StackPolicyURL: Optional[StackPolicyURL]
    Tags: Optional[Tags]
    ClientRequestToken: Optional[ClientRequestToken]
    EnableTerminationProtection: Optional[EnableTerminationProtection]


RegionList = List[Region]


class StackSetOperationPreferences(TypedDict, total=False):
    """The user-specified preferences for how CloudFormation performs a stack
    set operation.

    For more information on maximum concurrent accounts and failure
    tolerance, see `Stack set operation
    options <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options>`__.
    """

    RegionConcurrencyType: Optional[RegionConcurrencyType]
    RegionOrder: Optional[RegionList]
    FailureToleranceCount: Optional[FailureToleranceCount]
    FailureTolerancePercentage: Optional[FailureTolerancePercentage]
    MaxConcurrentCount: Optional[MaxConcurrentCount]
    MaxConcurrentPercentage: Optional[MaxConcurrentPercentage]


OrganizationalUnitIdList = List[OrganizationalUnitId]


class DeploymentTargets(TypedDict, total=False):
    """[Service-managed permissions] The Organizations accounts to which
    StackSets deploys. StackSets doesn't deploy stack instances to the
    organization management account, even if the organization management
    account is in your organization or in an OU in your organization.

    For update operations, you can specify either ``Accounts`` or
    ``OrganizationalUnitIds``. For create and delete operations, specify
    ``OrganizationalUnitIds``.
    """

    Accounts: Optional[AccountList]
    AccountsUrl: Optional[AccountsUrl]
    OrganizationalUnitIds: Optional[OrganizationalUnitIdList]


class CreateStackInstancesInput(ServiceRequest):
    StackSetName: StackSetName
    Accounts: Optional[AccountList]
    DeploymentTargets: Optional[DeploymentTargets]
    Regions: RegionList
    ParameterOverrides: Optional[Parameters]
    OperationPreferences: Optional[StackSetOperationPreferences]
    OperationId: Optional[ClientRequestToken]
    CallAs: Optional[CallAs]


class CreateStackInstancesOutput(TypedDict, total=False):
    OperationId: Optional[ClientRequestToken]


class CreateStackOutput(TypedDict, total=False):
    """The output for a CreateStack action."""

    StackId: Optional[StackId]


class ManagedExecution(TypedDict, total=False):
    """Describes whether StackSets performs non-conflicting operations
    concurrently and queues conflicting operations.
    """

    Active: Optional[ManagedExecutionNullable]


class CreateStackSetInput(ServiceRequest):
    StackSetName: StackSetName
    Description: Optional[Description]
    TemplateBody: Optional[TemplateBody]
    TemplateURL: Optional[TemplateURL]
    StackId: Optional[StackId]
    Parameters: Optional[Parameters]
    Capabilities: Optional[Capabilities]
    Tags: Optional[Tags]
    AdministrationRoleARN: Optional[RoleARN]
    ExecutionRoleName: Optional[ExecutionRoleName]
    PermissionModel: Optional[PermissionModels]
    AutoDeployment: Optional[AutoDeployment]
    CallAs: Optional[CallAs]
    ClientRequestToken: Optional[ClientRequestToken]
    ManagedExecution: Optional[ManagedExecution]


class CreateStackSetOutput(TypedDict, total=False):
    StackSetId: Optional[StackSetId]


class DeactivateTypeInput(ServiceRequest):
    TypeName: Optional[TypeName]
    Type: Optional[ThirdPartyType]
    Arn: Optional[PrivateTypeArn]


class DeactivateTypeOutput(TypedDict, total=False):
    pass


class DeleteChangeSetInput(ServiceRequest):
    """The input for the DeleteChangeSet action."""

    ChangeSetName: ChangeSetNameOrId
    StackName: Optional[StackNameOrId]


class DeleteChangeSetOutput(TypedDict, total=False):
    """The output for the DeleteChangeSet action."""

    pass


RetainResources = List[LogicalResourceId]


class DeleteStackInput(ServiceRequest):
    """The input for DeleteStack action."""

    StackName: StackName
    RetainResources: Optional[RetainResources]
    RoleARN: Optional[RoleARN]
    ClientRequestToken: Optional[ClientRequestToken]


class DeleteStackInstancesInput(ServiceRequest):
    StackSetName: StackSetName
    Accounts: Optional[AccountList]
    DeploymentTargets: Optional[DeploymentTargets]
    Regions: RegionList
    OperationPreferences: Optional[StackSetOperationPreferences]
    RetainStacks: RetainStacks
    OperationId: Optional[ClientRequestToken]
    CallAs: Optional[CallAs]


class DeleteStackInstancesOutput(TypedDict, total=False):
    OperationId: Optional[ClientRequestToken]


class DeleteStackSetInput(ServiceRequest):
    StackSetName: StackSetName
    CallAs: Optional[CallAs]


class DeleteStackSetOutput(TypedDict, total=False):
    pass


DeletionTime = datetime


class DeregisterTypeInput(ServiceRequest):
    Arn: Optional[PrivateTypeArn]
    Type: Optional[RegistryType]
    TypeName: Optional[TypeName]
    VersionId: Optional[TypeVersionId]


class DeregisterTypeOutput(TypedDict, total=False):
    pass


class DescribeAccountLimitsInput(ServiceRequest):
    """The input for the DescribeAccountLimits action."""

    NextToken: Optional[NextToken]


class DescribeAccountLimitsOutput(TypedDict, total=False):
    """The output for the DescribeAccountLimits action."""

    AccountLimits: Optional[AccountLimitList]
    NextToken: Optional[NextToken]


class DescribeChangeSetHooksInput(ServiceRequest):
    ChangeSetName: ChangeSetNameOrId
    StackName: Optional[StackNameOrId]
    NextToken: Optional[NextToken]
    LogicalResourceId: Optional[LogicalResourceId]


class DescribeChangeSetHooksOutput(TypedDict, total=False):
    ChangeSetId: Optional[ChangeSetId]
    ChangeSetName: Optional[ChangeSetName]
    Hooks: Optional[ChangeSetHooks]
    Status: Optional[ChangeSetHooksStatus]
    NextToken: Optional[NextToken]
    StackId: Optional[StackId]
    StackName: Optional[StackName]


class DescribeChangeSetInput(ServiceRequest):
    """The input for the DescribeChangeSet action."""

    ChangeSetName: ChangeSetNameOrId
    StackName: Optional[StackNameOrId]
    NextToken: Optional[NextToken]


class DescribeChangeSetOutput(TypedDict, total=False):
    """The output for the DescribeChangeSet action."""

    ChangeSetName: Optional[ChangeSetName]
    ChangeSetId: Optional[ChangeSetId]
    StackId: Optional[StackId]
    StackName: Optional[StackName]
    Description: Optional[Description]
    Parameters: Optional[Parameters]
    CreationTime: Optional[CreationTime]
    ExecutionStatus: Optional[ExecutionStatus]
    Status: Optional[ChangeSetStatus]
    StatusReason: Optional[ChangeSetStatusReason]
    NotificationARNs: Optional[NotificationARNs]
    RollbackConfiguration: Optional[RollbackConfiguration]
    Capabilities: Optional[Capabilities]
    Tags: Optional[Tags]
    Changes: Optional[Changes]
    NextToken: Optional[NextToken]
    IncludeNestedStacks: Optional[IncludeNestedStacks]
    ParentChangeSetId: Optional[ChangeSetId]
    RootChangeSetId: Optional[ChangeSetId]


class DescribePublisherInput(ServiceRequest):
    PublisherId: Optional[PublisherId]


class DescribePublisherOutput(TypedDict, total=False):
    PublisherId: Optional[PublisherId]
    PublisherStatus: Optional[PublisherStatus]
    IdentityProvider: Optional[IdentityProvider]
    PublisherProfile: Optional[PublisherProfile]


class DescribeStackDriftDetectionStatusInput(ServiceRequest):
    StackDriftDetectionId: StackDriftDetectionId


class DescribeStackDriftDetectionStatusOutput(TypedDict, total=False):
    StackId: StackId
    StackDriftDetectionId: StackDriftDetectionId
    StackDriftStatus: Optional[StackDriftStatus]
    DetectionStatus: StackDriftDetectionStatus
    DetectionStatusReason: Optional[StackDriftDetectionStatusReason]
    DriftedStackResourceCount: Optional[BoxedInteger]
    Timestamp: Timestamp


class DescribeStackEventsInput(ServiceRequest):
    """The input for DescribeStackEvents action."""

    StackName: Optional[StackName]
    NextToken: Optional[NextToken]


class StackEvent(TypedDict, total=False):
    """The StackEvent data type."""

    StackId: StackId
    EventId: EventId
    StackName: StackName
    LogicalResourceId: Optional[LogicalResourceId]
    PhysicalResourceId: Optional[PhysicalResourceId]
    ResourceType: Optional[ResourceType]
    Timestamp: Timestamp
    ResourceStatus: Optional[ResourceStatus]
    ResourceStatusReason: Optional[ResourceStatusReason]
    ResourceProperties: Optional[ResourceProperties]
    ClientRequestToken: Optional[ClientRequestToken]
    HookType: Optional[HookType]
    HookStatus: Optional[HookStatus]
    HookStatusReason: Optional[HookStatusReason]
    HookInvocationPoint: Optional[HookInvocationPoint]
    HookFailureMode: Optional[HookFailureMode]


StackEvents = List[StackEvent]


class DescribeStackEventsOutput(TypedDict, total=False):
    """The output for a DescribeStackEvents action."""

    StackEvents: Optional[StackEvents]
    NextToken: Optional[NextToken]


class DescribeStackInstanceInput(ServiceRequest):
    StackSetName: StackSetName
    StackInstanceAccount: Account
    StackInstanceRegion: Region
    CallAs: Optional[CallAs]


class StackInstanceComprehensiveStatus(TypedDict, total=False):
    """The detailed status of the stack instance."""

    DetailedStatus: Optional[StackInstanceDetailedStatus]


class StackInstance(TypedDict, total=False):
    """An CloudFormation stack, in a specific account and Region, that's part
    of a stack set operation. A stack instance is a reference to an
    attempted or actual stack in a given account within a given Region. A
    stack instance can exist without a stack—for example, if the stack
    couldn't be created for some reason. A stack instance is associated with
    only one stack set. Each stack instance contains the ID of its
    associated stack set, in addition to the ID of the actual stack and the
    stack status.
    """

    StackSetId: Optional[StackSetId]
    Region: Optional[Region]
    Account: Optional[Account]
    StackId: Optional[StackId]
    ParameterOverrides: Optional[Parameters]
    Status: Optional[StackInstanceStatus]
    StackInstanceStatus: Optional[StackInstanceComprehensiveStatus]
    StatusReason: Optional[Reason]
    OrganizationalUnitId: Optional[OrganizationalUnitId]
    DriftStatus: Optional[StackDriftStatus]
    LastDriftCheckTimestamp: Optional[Timestamp]


class DescribeStackInstanceOutput(TypedDict, total=False):
    StackInstance: Optional[StackInstance]


StackResourceDriftStatusFilters = List[StackResourceDriftStatus]


class DescribeStackResourceDriftsInput(ServiceRequest):
    StackName: StackNameOrId
    StackResourceDriftStatusFilters: Optional[StackResourceDriftStatusFilters]
    NextToken: Optional[NextToken]
    MaxResults: Optional[BoxedMaxResults]


class PropertyDifference(TypedDict, total=False):
    """Information about a resource property whose actual value differs from
    its expected value, as defined in the stack template and any values
    specified as template parameters. These will be present only for
    resources whose ``StackResourceDriftStatus`` is ``MODIFIED``. For more
    information, see `Detecting Unregulated Configuration Changes to Stacks
    and
    Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__.
    """

    PropertyPath: PropertyPath
    ExpectedValue: PropertyValue
    ActualValue: PropertyValue
    DifferenceType: DifferenceType


PropertyDifferences = List[PropertyDifference]


class PhysicalResourceIdContextKeyValuePair(TypedDict, total=False):
    """Context information that enables CloudFormation to uniquely identify a
    resource. CloudFormation uses context key-value pairs in cases where a
    resource's logical and physical IDs aren't enough to uniquely identify
    that resource. Each context key-value pair specifies a resource that
    contains the targeted resource.
    """

    Key: Key
    Value: Value


PhysicalResourceIdContext = List[PhysicalResourceIdContextKeyValuePair]


class StackResourceDrift(TypedDict, total=False):
    """Contains the drift information for a resource that has been checked for
    drift. This includes actual and expected property values for resources
    in which CloudFormation has detected drift. Only resource properties
    explicitly defined in the stack template are checked for drift. For more
    information, see `Detecting Unregulated Configuration Changes to Stacks
    and
    Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__.

    Resources that don't currently support drift detection can't be checked.
    For a list of resources that support drift detection, see `Resources
    that Support Drift
    Detection <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__.

    Use DetectStackResourceDrift to detect drift on individual resources, or
    DetectStackDrift to detect drift on all resources in a given stack that
    support drift detection.
    """

    StackId: StackId
    LogicalResourceId: LogicalResourceId
    PhysicalResourceId: Optional[PhysicalResourceId]
    PhysicalResourceIdContext: Optional[PhysicalResourceIdContext]
    ResourceType: ResourceType
    ExpectedProperties: Optional[Properties]
    ActualProperties: Optional[Properties]
    PropertyDifferences: Optional[PropertyDifferences]
    StackResourceDriftStatus: StackResourceDriftStatus
    Timestamp: Timestamp
    ModuleInfo: Optional[ModuleInfo]


StackResourceDrifts = List[StackResourceDrift]


class DescribeStackResourceDriftsOutput(TypedDict, total=False):
    StackResourceDrifts: StackResourceDrifts
    NextToken: Optional[NextToken]


class DescribeStackResourceInput(ServiceRequest):
    """The input for DescribeStackResource action."""

    StackName: StackName
    LogicalResourceId: LogicalResourceId


class StackResourceDriftInformation(TypedDict, total=False):
    """Contains information about whether the resource's actual configuration
    differs, or has *drifted*, from its expected configuration.
    """

    StackResourceDriftStatus: StackResourceDriftStatus
    LastCheckTimestamp: Optional[Timestamp]


class StackResourceDetail(TypedDict, total=False):
    """Contains detailed information about the specified stack resource."""

    StackName: Optional[StackName]
    StackId: Optional[StackId]
    LogicalResourceId: LogicalResourceId
    PhysicalResourceId: Optional[PhysicalResourceId]
    ResourceType: ResourceType
    LastUpdatedTimestamp: Timestamp
    ResourceStatus: ResourceStatus
    ResourceStatusReason: Optional[ResourceStatusReason]
    Description: Optional[Description]
    Metadata: Optional[Metadata]
    DriftInformation: Optional[StackResourceDriftInformation]
    ModuleInfo: Optional[ModuleInfo]


class DescribeStackResourceOutput(TypedDict, total=False):
    """The output for a DescribeStackResource action."""

    StackResourceDetail: Optional[StackResourceDetail]


class DescribeStackResourcesInput(ServiceRequest):
    """The input for DescribeStackResources action."""

    StackName: Optional[StackName]
    LogicalResourceId: Optional[LogicalResourceId]
    PhysicalResourceId: Optional[PhysicalResourceId]


class StackResource(TypedDict, total=False):
    """The StackResource data type."""

    StackName: Optional[StackName]
    StackId: Optional[StackId]
    LogicalResourceId: LogicalResourceId
    PhysicalResourceId: Optional[PhysicalResourceId]
    ResourceType: ResourceType
    Timestamp: Timestamp
    ResourceStatus: ResourceStatus
    ResourceStatusReason: Optional[ResourceStatusReason]
    Description: Optional[Description]
    DriftInformation: Optional[StackResourceDriftInformation]
    ModuleInfo: Optional[ModuleInfo]


StackResources = List[StackResource]


class DescribeStackResourcesOutput(TypedDict, total=False):
    """The output for a DescribeStackResources action."""

    StackResources: Optional[StackResources]


class DescribeStackSetInput(ServiceRequest):
    StackSetName: StackSetName
    CallAs: Optional[CallAs]


class DescribeStackSetOperationInput(ServiceRequest):
    StackSetName: StackSetName
    OperationId: ClientRequestToken
    CallAs: Optional[CallAs]


class StackSetDriftDetectionDetails(TypedDict, total=False):
    """Detailed information about the drift status of the stack set.

    For stack sets, contains information about the last *completed* drift
    operation performed on the stack set. Information about drift operations
    in-progress isn't included.

    For stack set operations, includes information about drift operations
    currently being performed on the stack set.

    For more information, see `Detecting unmanaged changes in stack
    sets <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html>`__
    in the *CloudFormation User Guide*.
    """

    DriftStatus: Optional[StackSetDriftStatus]
    DriftDetectionStatus: Optional[StackSetDriftDetectionStatus]
    LastDriftCheckTimestamp: Optional[Timestamp]
    TotalStackInstancesCount: Optional[TotalStackInstancesCount]
    DriftedStackInstancesCount: Optional[DriftedStackInstancesCount]
    InSyncStackInstancesCount: Optional[InSyncStackInstancesCount]
    InProgressStackInstancesCount: Optional[InProgressStackInstancesCount]
    FailedStackInstancesCount: Optional[FailedStackInstancesCount]


class StackSetOperation(TypedDict, total=False):
    """The structure that contains information about a stack set operation."""

    OperationId: Optional[ClientRequestToken]
    StackSetId: Optional[StackSetId]
    Action: Optional[StackSetOperationAction]
    Status: Optional[StackSetOperationStatus]
    OperationPreferences: Optional[StackSetOperationPreferences]
    RetainStacks: Optional[RetainStacksNullable]
    AdministrationRoleARN: Optional[RoleARN]
    ExecutionRoleName: Optional[ExecutionRoleName]
    CreationTimestamp: Optional[Timestamp]
    EndTimestamp: Optional[Timestamp]
    DeploymentTargets: Optional[DeploymentTargets]
    StackSetDriftDetectionDetails: Optional[StackSetDriftDetectionDetails]


class DescribeStackSetOperationOutput(TypedDict, total=False):
    StackSetOperation: Optional[StackSetOperation]


class StackSet(TypedDict, total=False):
    """A structure that contains information about a stack set. A stack set
    enables you to provision stacks into Amazon Web Services accounts and
    across Regions by using a single CloudFormation template. In the stack
    set, you specify the template to use, in addition to any parameters and
    capabilities that the template requires.
    """

    StackSetName: Optional[StackSetName]
    StackSetId: Optional[StackSetId]
    Description: Optional[Description]
    Status: Optional[StackSetStatus]
    TemplateBody: Optional[TemplateBody]
    Parameters: Optional[Parameters]
    Capabilities: Optional[Capabilities]
    Tags: Optional[Tags]
    StackSetARN: Optional[StackSetARN]
    AdministrationRoleARN: Optional[RoleARN]
    ExecutionRoleName: Optional[ExecutionRoleName]
    StackSetDriftDetectionDetails: Optional[StackSetDriftDetectionDetails]
    AutoDeployment: Optional[AutoDeployment]
    PermissionModel: Optional[PermissionModels]
    OrganizationalUnitIds: Optional[OrganizationalUnitIdList]
    ManagedExecution: Optional[ManagedExecution]


class DescribeStackSetOutput(TypedDict, total=False):
    StackSet: Optional[StackSet]


class DescribeStacksInput(ServiceRequest):
    """The input for DescribeStacks action."""

    StackName: Optional[StackName]
    NextToken: Optional[NextToken]


class StackDriftInformation(TypedDict, total=False):
    """Contains information about whether the stack's actual configuration
    differs, or has *drifted*, from its expected configuration, as defined
    in the stack template and any values specified as template parameters. A
    stack is considered to have drifted if one or more of its resources have
    drifted.
    """

    StackDriftStatus: StackDriftStatus
    LastCheckTimestamp: Optional[Timestamp]


class Output(TypedDict, total=False):
    """The Output data type."""

    OutputKey: Optional[OutputKey]
    OutputValue: Optional[OutputValue]
    Description: Optional[Description]
    ExportName: Optional[ExportName]


Outputs = List[Output]
LastUpdatedTime = datetime


class Stack(TypedDict, total=False):
    """The Stack data type."""

    StackId: Optional[StackId]
    StackName: StackName
    ChangeSetId: Optional[ChangeSetId]
    Description: Optional[Description]
    Parameters: Optional[Parameters]
    CreationTime: CreationTime
    DeletionTime: Optional[DeletionTime]
    LastUpdatedTime: Optional[LastUpdatedTime]
    RollbackConfiguration: Optional[RollbackConfiguration]
    StackStatus: StackStatus
    StackStatusReason: Optional[StackStatusReason]
    DisableRollback: Optional[DisableRollback]
    NotificationARNs: Optional[NotificationARNs]
    TimeoutInMinutes: Optional[TimeoutMinutes]
    Capabilities: Optional[Capabilities]
    Outputs: Optional[Outputs]
    RoleARN: Optional[RoleARN]
    Tags: Optional[Tags]
    EnableTerminationProtection: Optional[EnableTerminationProtection]
    ParentId: Optional[StackId]
    RootId: Optional[StackId]
    DriftInformation: Optional[StackDriftInformation]


Stacks = List[Stack]


class DescribeStacksOutput(TypedDict, total=False):
    """The output for a DescribeStacks action."""

    Stacks: Optional[Stacks]
    NextToken: Optional[NextToken]


class DescribeTypeInput(ServiceRequest):
    Type: Optional[RegistryType]
    TypeName: Optional[TypeName]
    Arn: Optional[TypeArn]
    VersionId: Optional[TypeVersionId]
    PublisherId: Optional[PublisherId]
    PublicVersionNumber: Optional[PublicVersionNumber]


SupportedMajorVersions = List[SupportedMajorVersion]


class RequiredActivatedType(TypedDict, total=False):
    """For extensions that are modules, a public third-party extension that
    must be activated in your account in order for the module itself to be
    activated.

    For more information, see `Activating public modules for use in your
    account <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html#module-enabling>`__
    in the *CloudFormation User Guide*.
    """

    TypeNameAlias: Optional[TypeName]
    OriginalTypeName: Optional[TypeName]
    PublisherId: Optional[PublisherId]
    SupportedMajorVersions: Optional[SupportedMajorVersions]


RequiredActivatedTypes = List[RequiredActivatedType]


class DescribeTypeOutput(TypedDict, total=False):
    Arn: Optional[TypeArn]
    Type: Optional[RegistryType]
    TypeName: Optional[TypeName]
    DefaultVersionId: Optional[TypeVersionId]
    IsDefaultVersion: Optional[IsDefaultVersion]
    TypeTestsStatus: Optional[TypeTestsStatus]
    TypeTestsStatusDescription: Optional[TypeTestsStatusDescription]
    Description: Optional[Description]
    Schema: Optional[TypeSchema]
    ProvisioningType: Optional[ProvisioningType]
    DeprecatedStatus: Optional[DeprecatedStatus]
    LoggingConfig: Optional[LoggingConfig]
    RequiredActivatedTypes: Optional[RequiredActivatedTypes]
    ExecutionRoleArn: Optional[RoleArn]
    Visibility: Optional[Visibility]
    SourceUrl: Optional[OptionalSecureUrl]
    DocumentationUrl: Optional[OptionalSecureUrl]
    LastUpdated: Optional[Timestamp]
    TimeCreated: Optional[Timestamp]
    ConfigurationSchema: Optional[ConfigurationSchema]
    PublisherId: Optional[PublisherId]
    OriginalTypeName: Optional[TypeName]
    OriginalTypeArn: Optional[TypeArn]
    PublicVersionNumber: Optional[PublicVersionNumber]
    LatestPublicVersion: Optional[PublicVersionNumber]
    IsActivated: Optional[IsActivated]
    AutoUpdate: Optional[AutoUpdate]


class DescribeTypeRegistrationInput(ServiceRequest):
    RegistrationToken: RegistrationToken


class DescribeTypeRegistrationOutput(TypedDict, total=False):
    ProgressStatus: Optional[RegistrationStatus]
    Description: Optional[Description]
    TypeArn: Optional[TypeArn]
    TypeVersionArn: Optional[TypeArn]


LogicalResourceIds = List[LogicalResourceId]


class DetectStackDriftInput(ServiceRequest):
    StackName: StackNameOrId
    LogicalResourceIds: Optional[LogicalResourceIds]


class DetectStackDriftOutput(TypedDict, total=False):
    StackDriftDetectionId: StackDriftDetectionId


class DetectStackResourceDriftInput(ServiceRequest):
    StackName: StackNameOrId
    LogicalResourceId: LogicalResourceId


class DetectStackResourceDriftOutput(TypedDict, total=False):
    StackResourceDrift: StackResourceDrift


class DetectStackSetDriftInput(ServiceRequest):
    StackSetName: StackSetNameOrId
    OperationPreferences: Optional[StackSetOperationPreferences]
    OperationId: Optional[ClientRequestToken]
    CallAs: Optional[CallAs]


class DetectStackSetDriftOutput(TypedDict, total=False):
    OperationId: Optional[ClientRequestToken]


class EstimateTemplateCostInput(ServiceRequest):
    """The input for an EstimateTemplateCost action."""

    TemplateBody: Optional[TemplateBody]
    TemplateURL: Optional[TemplateURL]
    Parameters: Optional[Parameters]


class EstimateTemplateCostOutput(TypedDict, total=False):
    """The output for a EstimateTemplateCost action."""

    Url: Optional[Url]


class ExecuteChangeSetInput(ServiceRequest):
    """The input for the ExecuteChangeSet action."""

    ChangeSetName: ChangeSetNameOrId
    StackName: Optional[StackNameOrId]
    ClientRequestToken: Optional[ClientRequestToken]
    DisableRollback: Optional[DisableRollback]


class ExecuteChangeSetOutput(TypedDict, total=False):
    """The output for the ExecuteChangeSet action."""

    pass


class Export(TypedDict, total=False):
    """The ``Export`` structure describes the exported output values for a
    stack.
    """

    ExportingStackId: Optional[StackId]
    Name: Optional[ExportName]
    Value: Optional[ExportValue]


Exports = List[Export]


class GetStackPolicyInput(ServiceRequest):
    """The input for the GetStackPolicy action."""

    StackName: StackName


class GetStackPolicyOutput(TypedDict, total=False):
    """The output for the GetStackPolicy action."""

    StackPolicyBody: Optional[StackPolicyBody]


class GetTemplateInput(ServiceRequest):
    """The input for a GetTemplate action."""

    StackName: Optional[StackName]
    ChangeSetName: Optional[ChangeSetNameOrId]
    TemplateStage: Optional[TemplateStage]


StageList = List[TemplateStage]


class GetTemplateOutput(TypedDict, total=False):
    """The output for GetTemplate action."""

    TemplateBody: Optional[TemplateBody]
    StagesAvailable: Optional[StageList]


class GetTemplateSummaryInput(ServiceRequest):
    """The input for the GetTemplateSummary action."""

    TemplateBody: Optional[TemplateBody]
    TemplateURL: Optional[TemplateURL]
    StackName: Optional[StackNameOrId]
    StackSetName: Optional[StackSetNameOrId]
    CallAs: Optional[CallAs]


ResourceIdentifiers = List[ResourceIdentifierPropertyKey]


class ResourceIdentifierSummary(TypedDict, total=False):
    """Describes the target resources of a specific type in your import
    template (for example, all ``AWS::S3::Bucket`` resources) and the
    properties you can provide during the import to identify resources of
    that type.
    """

    ResourceType: Optional[ResourceType]
    LogicalResourceIds: Optional[LogicalResourceIds]
    ResourceIdentifiers: Optional[ResourceIdentifiers]


ResourceIdentifierSummaries = List[ResourceIdentifierSummary]
TransformsList = List[TransformName]


class ParameterConstraints(TypedDict, total=False):
    """A set of criteria that CloudFormation uses to validate parameter values.
    Although other constraints might be defined in the stack template,
    CloudFormation returns only the ``AllowedValues`` property.
    """

    AllowedValues: Optional[AllowedValues]


class ParameterDeclaration(TypedDict, total=False):
    """The ParameterDeclaration data type."""

    ParameterKey: Optional[ParameterKey]
    DefaultValue: Optional[ParameterValue]
    ParameterType: Optional[ParameterType]
    NoEcho: Optional[NoEcho]
    Description: Optional[Description]
    ParameterConstraints: Optional[ParameterConstraints]


ParameterDeclarations = List[ParameterDeclaration]


class GetTemplateSummaryOutput(TypedDict, total=False):
    """The output for the GetTemplateSummary action."""

    Parameters: Optional[ParameterDeclarations]
    Description: Optional[Description]
    Capabilities: Optional[Capabilities]
    CapabilitiesReason: Optional[CapabilitiesReason]
    ResourceTypes: Optional[ResourceTypes]
    Version: Optional[Version]
    Metadata: Optional[Metadata]
    DeclaredTransforms: Optional[TransformsList]
    ResourceIdentifierSummaries: Optional[ResourceIdentifierSummaries]


StackIdList = List[StackId]


class ImportStacksToStackSetInput(ServiceRequest):
    StackSetName: StackSetNameOrId
    StackIds: Optional[StackIdList]
    StackIdsUrl: Optional[StackIdsUrl]
    OrganizationalUnitIds: Optional[OrganizationalUnitIdList]
    OperationPreferences: Optional[StackSetOperationPreferences]
    OperationId: Optional[ClientRequestToken]
    CallAs: Optional[CallAs]


class ImportStacksToStackSetOutput(TypedDict, total=False):
    OperationId: Optional[ClientRequestToken]


Imports = List[StackName]


class ListChangeSetsInput(ServiceRequest):
    """The input for the ListChangeSets action."""

    StackName: StackNameOrId
    NextToken: Optional[NextToken]


class ListChangeSetsOutput(TypedDict, total=False):
    """The output for the ListChangeSets action."""

    Summaries: Optional[ChangeSetSummaries]
    NextToken: Optional[NextToken]


class ListExportsInput(ServiceRequest):
    NextToken: Optional[NextToken]


class ListExportsOutput(TypedDict, total=False):
    Exports: Optional[Exports]
    NextToken: Optional[NextToken]


class ListImportsInput(ServiceRequest):
    ExportName: ExportName
    NextToken: Optional[NextToken]


class ListImportsOutput(TypedDict, total=False):
    Imports: Optional[Imports]
    NextToken: Optional[NextToken]


class StackInstanceFilter(TypedDict, total=False):
    """The status that stack instances are filtered by."""

    Name: Optional[StackInstanceFilterName]
    Values: Optional[StackInstanceFilterValues]


StackInstanceFilters = List[StackInstanceFilter]


class ListStackInstancesInput(ServiceRequest):
    StackSetName: StackSetName
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    Filters: Optional[StackInstanceFilters]
    StackInstanceAccount: Optional[Account]
    StackInstanceRegion: Optional[Region]
    CallAs: Optional[CallAs]


class StackInstanceSummary(TypedDict, total=False):
    """The structure that contains summary information about a stack instance."""

    StackSetId: Optional[StackSetId]
    Region: Optional[Region]
    Account: Optional[Account]
    StackId: Optional[StackId]
    Status: Optional[StackInstanceStatus]
    StatusReason: Optional[Reason]
    StackInstanceStatus: Optional[StackInstanceComprehensiveStatus]
    OrganizationalUnitId: Optional[OrganizationalUnitId]
    DriftStatus: Optional[StackDriftStatus]
    LastDriftCheckTimestamp: Optional[Timestamp]


StackInstanceSummaries = List[StackInstanceSummary]


class ListStackInstancesOutput(TypedDict, total=False):
    Summaries: Optional[StackInstanceSummaries]
    NextToken: Optional[NextToken]


class ListStackResourcesInput(ServiceRequest):
    """The input for the ListStackResource action."""

    StackName: StackName
    NextToken: Optional[NextToken]


class StackResourceDriftInformationSummary(TypedDict, total=False):
    """Summarizes information about whether the resource's actual configuration
    differs, or has *drifted*, from its expected configuration.
    """

    StackResourceDriftStatus: StackResourceDriftStatus
    LastCheckTimestamp: Optional[Timestamp]


class StackResourceSummary(TypedDict, total=False):
    """Contains high-level information about the specified stack resource."""

    LogicalResourceId: LogicalResourceId
    PhysicalResourceId: Optional[PhysicalResourceId]
    ResourceType: ResourceType
    LastUpdatedTimestamp: Timestamp
    ResourceStatus: ResourceStatus
    ResourceStatusReason: Optional[ResourceStatusReason]
    DriftInformation: Optional[StackResourceDriftInformationSummary]
    ModuleInfo: Optional[ModuleInfo]


StackResourceSummaries = List[StackResourceSummary]


class ListStackResourcesOutput(TypedDict, total=False):
    """The output for a ListStackResources action."""

    StackResourceSummaries: Optional[StackResourceSummaries]
    NextToken: Optional[NextToken]


class ListStackSetOperationResultsInput(ServiceRequest):
    StackSetName: StackSetName
    OperationId: ClientRequestToken
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    CallAs: Optional[CallAs]


class StackSetOperationResultSummary(TypedDict, total=False):
    """The structure that contains information about a specified operation's
    results for a given account in a given Region.
    """

    Account: Optional[Account]
    Region: Optional[Region]
    Status: Optional[StackSetOperationResultStatus]
    StatusReason: Optional[Reason]
    AccountGateResult: Optional[AccountGateResult]
    OrganizationalUnitId: Optional[OrganizationalUnitId]


StackSetOperationResultSummaries = List[StackSetOperationResultSummary]


class ListStackSetOperationResultsOutput(TypedDict, total=False):
    Summaries: Optional[StackSetOperationResultSummaries]
    NextToken: Optional[NextToken]


class ListStackSetOperationsInput(ServiceRequest):
    StackSetName: StackSetName
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    CallAs: Optional[CallAs]


class StackSetOperationSummary(TypedDict, total=False):
    """The structures that contain summary information about the specified
    operation.
    """

    OperationId: Optional[ClientRequestToken]
    Action: Optional[StackSetOperationAction]
    Status: Optional[StackSetOperationStatus]
    CreationTimestamp: Optional[Timestamp]
    EndTimestamp: Optional[Timestamp]


StackSetOperationSummaries = List[StackSetOperationSummary]


class ListStackSetOperationsOutput(TypedDict, total=False):
    Summaries: Optional[StackSetOperationSummaries]
    NextToken: Optional[NextToken]


class ListStackSetsInput(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]
    Status: Optional[StackSetStatus]
    CallAs: Optional[CallAs]


class StackSetSummary(TypedDict, total=False):
    """The structures that contain summary information about the specified
    stack set.
    """

    StackSetName: Optional[StackSetName]
    StackSetId: Optional[StackSetId]
    Description: Optional[Description]
    Status: Optional[StackSetStatus]
    AutoDeployment: Optional[AutoDeployment]
    PermissionModel: Optional[PermissionModels]
    DriftStatus: Optional[StackDriftStatus]
    LastDriftCheckTimestamp: Optional[Timestamp]
    ManagedExecution: Optional[ManagedExecution]


StackSetSummaries = List[StackSetSummary]


class ListStackSetsOutput(TypedDict, total=False):
    Summaries: Optional[StackSetSummaries]
    NextToken: Optional[NextToken]


StackStatusFilter = List[StackStatus]


class ListStacksInput(ServiceRequest):
    """The input for ListStacks action."""

    NextToken: Optional[NextToken]
    StackStatusFilter: Optional[StackStatusFilter]


class StackDriftInformationSummary(TypedDict, total=False):
    """Contains information about whether the stack's actual configuration
    differs, or has *drifted*, from its expected configuration, as defined
    in the stack template and any values specified as template parameters. A
    stack is considered to have drifted if one or more of its resources have
    drifted.
    """

    StackDriftStatus: StackDriftStatus
    LastCheckTimestamp: Optional[Timestamp]


class StackSummary(TypedDict, total=False):
    """The StackSummary Data Type"""

    StackId: Optional[StackId]
    StackName: StackName
    TemplateDescription: Optional[TemplateDescription]
    CreationTime: CreationTime
    LastUpdatedTime: Optional[LastUpdatedTime]
    DeletionTime: Optional[DeletionTime]
    StackStatus: StackStatus
    StackStatusReason: Optional[StackStatusReason]
    ParentId: Optional[StackId]
    RootId: Optional[StackId]
    DriftInformation: Optional[StackDriftInformationSummary]


StackSummaries = List[StackSummary]


class ListStacksOutput(TypedDict, total=False):
    """The output for ListStacks action."""

    StackSummaries: Optional[StackSummaries]
    NextToken: Optional[NextToken]


class ListTypeRegistrationsInput(ServiceRequest):
    Type: Optional[RegistryType]
    TypeName: Optional[TypeName]
    TypeArn: Optional[TypeArn]
    RegistrationStatusFilter: Optional[RegistrationStatus]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


RegistrationTokenList = List[RegistrationToken]


class ListTypeRegistrationsOutput(TypedDict, total=False):
    RegistrationTokenList: Optional[RegistrationTokenList]
    NextToken: Optional[NextToken]


class ListTypeVersionsInput(ServiceRequest):
    Type: Optional[RegistryType]
    TypeName: Optional[TypeName]
    Arn: Optional[TypeArn]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]
    DeprecatedStatus: Optional[DeprecatedStatus]
    PublisherId: Optional[PublisherId]


class TypeVersionSummary(TypedDict, total=False):
    """Contains summary information about a specific version of a
    CloudFormation extension.
    """

    Type: Optional[RegistryType]
    TypeName: Optional[TypeName]
    VersionId: Optional[TypeVersionId]
    IsDefaultVersion: Optional[IsDefaultVersion]
    Arn: Optional[TypeArn]
    TimeCreated: Optional[Timestamp]
    Description: Optional[Description]
    PublicVersionNumber: Optional[PublicVersionNumber]


TypeVersionSummaries = List[TypeVersionSummary]


class ListTypeVersionsOutput(TypedDict, total=False):
    TypeVersionSummaries: Optional[TypeVersionSummaries]
    NextToken: Optional[NextToken]


class TypeFilters(TypedDict, total=False):
    """Filter criteria to use in determining which extensions to return."""

    Category: Optional[Category]
    PublisherId: Optional[PublisherId]
    TypeNamePrefix: Optional[TypeNamePrefix]


class ListTypesInput(ServiceRequest):
    Visibility: Optional[Visibility]
    ProvisioningType: Optional[ProvisioningType]
    DeprecatedStatus: Optional[DeprecatedStatus]
    Type: Optional[RegistryType]
    Filters: Optional[TypeFilters]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class TypeSummary(TypedDict, total=False):
    """Contains summary information about the specified CloudFormation
    extension.
    """

    Type: Optional[RegistryType]
    TypeName: Optional[TypeName]
    DefaultVersionId: Optional[TypeVersionId]
    TypeArn: Optional[TypeArn]
    LastUpdated: Optional[Timestamp]
    Description: Optional[Description]
    PublisherId: Optional[PublisherId]
    OriginalTypeName: Optional[TypeName]
    PublicVersionNumber: Optional[PublicVersionNumber]
    LatestPublicVersion: Optional[PublicVersionNumber]
    PublisherIdentity: Optional[IdentityProvider]
    PublisherName: Optional[PublisherName]
    IsActivated: Optional[IsActivated]


TypeSummaries = List[TypeSummary]


class ListTypesOutput(TypedDict, total=False):
    TypeSummaries: Optional[TypeSummaries]
    NextToken: Optional[NextToken]


class PublishTypeInput(ServiceRequest):
    Type: Optional[ThirdPartyType]
    Arn: Optional[PrivateTypeArn]
    TypeName: Optional[TypeName]
    PublicVersionNumber: Optional[PublicVersionNumber]


class PublishTypeOutput(TypedDict, total=False):
    PublicTypeArn: Optional[TypeArn]


class RecordHandlerProgressInput(ServiceRequest):
    BearerToken: ClientToken
    OperationStatus: OperationStatus
    CurrentOperationStatus: Optional[OperationStatus]
    StatusMessage: Optional[StatusMessage]
    ErrorCode: Optional[HandlerErrorCode]
    ResourceModel: Optional[ResourceModel]
    ClientRequestToken: Optional[ClientRequestToken]


class RecordHandlerProgressOutput(TypedDict, total=False):
    pass


class RegisterPublisherInput(ServiceRequest):
    AcceptTermsAndConditions: Optional[AcceptTermsAndConditions]
    ConnectionArn: Optional[ConnectionArn]


class RegisterPublisherOutput(TypedDict, total=False):
    PublisherId: Optional[PublisherId]


class RegisterTypeInput(ServiceRequest):
    Type: Optional[RegistryType]
    TypeName: TypeName
    SchemaHandlerPackage: S3Url
    LoggingConfig: Optional[LoggingConfig]
    ExecutionRoleArn: Optional[RoleArn]
    ClientRequestToken: Optional[RequestToken]


class RegisterTypeOutput(TypedDict, total=False):
    RegistrationToken: Optional[RegistrationToken]


class RollbackStackInput(ServiceRequest):
    StackName: StackNameOrId
    RoleARN: Optional[RoleARN]
    ClientRequestToken: Optional[ClientRequestToken]


class RollbackStackOutput(TypedDict, total=False):
    StackId: Optional[StackId]


class SetStackPolicyInput(ServiceRequest):
    """The input for the SetStackPolicy action."""

    StackName: StackName
    StackPolicyBody: Optional[StackPolicyBody]
    StackPolicyURL: Optional[StackPolicyURL]


class SetTypeConfigurationInput(ServiceRequest):
    TypeArn: Optional[TypeArn]
    Configuration: TypeConfiguration
    ConfigurationAlias: Optional[TypeConfigurationAlias]
    TypeName: Optional[TypeName]
    Type: Optional[ThirdPartyType]


class SetTypeConfigurationOutput(TypedDict, total=False):
    ConfigurationArn: Optional[TypeConfigurationArn]


class SetTypeDefaultVersionInput(ServiceRequest):
    Arn: Optional[PrivateTypeArn]
    Type: Optional[RegistryType]
    TypeName: Optional[TypeName]
    VersionId: Optional[TypeVersionId]


class SetTypeDefaultVersionOutput(TypedDict, total=False):
    pass


class SignalResourceInput(ServiceRequest):
    """The input for the SignalResource action."""

    StackName: StackNameOrId
    LogicalResourceId: LogicalResourceId
    UniqueId: ResourceSignalUniqueId
    Status: ResourceSignalStatus


class StopStackSetOperationInput(ServiceRequest):
    StackSetName: StackSetName
    OperationId: ClientRequestToken
    CallAs: Optional[CallAs]


class StopStackSetOperationOutput(TypedDict, total=False):
    pass


class TemplateParameter(TypedDict, total=False):
    """The TemplateParameter data type."""

    ParameterKey: Optional[ParameterKey]
    DefaultValue: Optional[ParameterValue]
    NoEcho: Optional[NoEcho]
    Description: Optional[Description]


TemplateParameters = List[TemplateParameter]


class TestTypeInput(ServiceRequest):
    Arn: Optional[TypeArn]
    Type: Optional[ThirdPartyType]
    TypeName: Optional[TypeName]
    VersionId: Optional[TypeVersionId]
    LogDeliveryBucket: Optional[S3Bucket]


class TestTypeOutput(TypedDict, total=False):
    TypeVersionArn: Optional[TypeArn]


class UpdateStackInput(ServiceRequest):
    """The input for an UpdateStack action."""

    StackName: StackName
    TemplateBody: Optional[TemplateBody]
    TemplateURL: Optional[TemplateURL]
    UsePreviousTemplate: Optional[UsePreviousTemplate]
    StackPolicyDuringUpdateBody: Optional[StackPolicyDuringUpdateBody]
    StackPolicyDuringUpdateURL: Optional[StackPolicyDuringUpdateURL]
    Parameters: Optional[Parameters]
    Capabilities: Optional[Capabilities]
    ResourceTypes: Optional[ResourceTypes]
    RoleARN: Optional[RoleARN]
    RollbackConfiguration: Optional[RollbackConfiguration]
    StackPolicyBody: Optional[StackPolicyBody]
    StackPolicyURL: Optional[StackPolicyURL]
    NotificationARNs: Optional[NotificationARNs]
    Tags: Optional[Tags]
    DisableRollback: Optional[DisableRollback]
    ClientRequestToken: Optional[ClientRequestToken]


class UpdateStackInstancesInput(ServiceRequest):
    StackSetName: StackSetNameOrId
    Accounts: Optional[AccountList]
    DeploymentTargets: Optional[DeploymentTargets]
    Regions: RegionList
    ParameterOverrides: Optional[Parameters]
    OperationPreferences: Optional[StackSetOperationPreferences]
    OperationId: Optional[ClientRequestToken]
    CallAs: Optional[CallAs]


class UpdateStackInstancesOutput(TypedDict, total=False):
    OperationId: Optional[ClientRequestToken]


class UpdateStackOutput(TypedDict, total=False):
    """The output for an UpdateStack action."""

    StackId: Optional[StackId]


class UpdateStackSetInput(ServiceRequest):
    StackSetName: StackSetName
    Description: Optional[Description]
    TemplateBody: Optional[TemplateBody]
    TemplateURL: Optional[TemplateURL]
    UsePreviousTemplate: Optional[UsePreviousTemplate]
    Parameters: Optional[Parameters]
    Capabilities: Optional[Capabilities]
    Tags: Optional[Tags]
    OperationPreferences: Optional[StackSetOperationPreferences]
    AdministrationRoleARN: Optional[RoleARN]
    ExecutionRoleName: Optional[ExecutionRoleName]
    DeploymentTargets: Optional[DeploymentTargets]
    PermissionModel: Optional[PermissionModels]
    AutoDeployment: Optional[AutoDeployment]
    OperationId: Optional[ClientRequestToken]
    Accounts: Optional[AccountList]
    Regions: Optional[RegionList]
    CallAs: Optional[CallAs]
    ManagedExecution: Optional[ManagedExecution]


class UpdateStackSetOutput(TypedDict, total=False):
    OperationId: Optional[ClientRequestToken]


class UpdateTerminationProtectionInput(ServiceRequest):
    EnableTerminationProtection: EnableTerminationProtection
    StackName: StackNameOrId


class UpdateTerminationProtectionOutput(TypedDict, total=False):
    StackId: Optional[StackId]


class ValidateTemplateInput(ServiceRequest):
    """The input for ValidateTemplate action."""

    TemplateBody: Optional[TemplateBody]
    TemplateURL: Optional[TemplateURL]


class ValidateTemplateOutput(TypedDict, total=False):
    """The output for ValidateTemplate action."""

    Parameters: Optional[TemplateParameters]
    Description: Optional[Description]
    Capabilities: Optional[Capabilities]
    CapabilitiesReason: Optional[CapabilitiesReason]
    DeclaredTransforms: Optional[TransformsList]


class CloudformationApi:

    service = "cloudformation"
    version = "2010-05-15"

    @handler("ActivateType", expand=False)
    def activate_type(
        self, context: RequestContext, request: ActivateTypeInput
    ) -> ActivateTypeOutput:
        """Activates a public third-party extension, making it available for use in
        stack templates. For more information, see `Using public
        extensions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html>`__
        in the *CloudFormation User Guide*.

        Once you have activated a public third-party extension in your account
        and region, use
        `SetTypeConfiguration <AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html>`__
        to specify configuration properties for the extension. For more
        information, see `Configuring extensions at the account
        level <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration>`__
        in the *CloudFormation User Guide*.

        :param type: The extension type.
        :param public_type_arn: The Amazon Resource Number (ARN) of the public extension.
        :param publisher_id: The ID of the extension publisher.
        :param type_name: The name of the extension.
        :param type_name_alias: An alias to assign to the public extension, in this account and region.
        :param auto_update: Whether to automatically update the extension in this account and region
        when a new *minor* version is published by the extension publisher.
        :param logging_config: Contains logging configuration information for an extension.
        :param execution_role_arn: The name of the IAM execution role to use to activate the extension.
        :param version_bump: Manually updates a previously-activated type to a new major or minor
        version, if available.
        :param major_version: The major version of this extension you want to activate, if multiple
        major versions are available.
        :returns: ActivateTypeOutput
        :raises CFNRegistryException:
        :raises TypeNotFoundException:
        """
        raise NotImplementedError

    @handler("BatchDescribeTypeConfigurations")
    def batch_describe_type_configurations(
        self,
        context: RequestContext,
        type_configuration_identifiers: TypeConfigurationIdentifiers,
    ) -> BatchDescribeTypeConfigurationsOutput:
        """Returns configuration data for the specified CloudFormation extensions,
        from the CloudFormation registry for the account and region.

        For more information, see `Configuring extensions at the account
        level <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration>`__
        in the *CloudFormation User Guide*.

        :param type_configuration_identifiers: The list of identifiers for the desired extension configurations.
        :returns: BatchDescribeTypeConfigurationsOutput
        :raises TypeConfigurationNotFoundException:
        :raises CFNRegistryException:
        """
        raise NotImplementedError

    @handler("CancelUpdateStack")
    def cancel_update_stack(
        self,
        context: RequestContext,
        stack_name: StackName,
        client_request_token: ClientRequestToken = None,
    ) -> None:
        """Cancels an update on the specified stack. If the call completes
        successfully, the stack rolls back the update and reverts to the
        previous stack configuration.

        You can cancel only stacks that are in the ``UPDATE_IN_PROGRESS`` state.

        :param stack_name: The name or the unique stack ID that's associated with the stack.
        :param client_request_token: A unique identifier for this ``CancelUpdateStack`` request.
        :raises TokenAlreadyExistsException:
        """
        raise NotImplementedError

    @handler("ContinueUpdateRollback")
    def continue_update_rollback(
        self,
        context: RequestContext,
        stack_name: StackNameOrId,
        role_arn: RoleARN = None,
        resources_to_skip: ResourcesToSkip = None,
        client_request_token: ClientRequestToken = None,
    ) -> ContinueUpdateRollbackOutput:
        """For a specified stack that's in the ``UPDATE_ROLLBACK_FAILED`` state,
        continues rolling it back to the ``UPDATE_ROLLBACK_COMPLETE`` state.
        Depending on the cause of the failure, you can manually `fix the
        error <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed>`__
        and continue the rollback. By continuing the rollback, you can return
        your stack to a working state (the ``UPDATE_ROLLBACK_COMPLETE`` state),
        and then try to update the stack again.

        A stack goes into the ``UPDATE_ROLLBACK_FAILED`` state when
        CloudFormation can't roll back all changes after a failed stack update.
        For example, you might have a stack that's rolling back to an old
        database instance that was deleted outside of CloudFormation. Because
        CloudFormation doesn't know the database was deleted, it assumes that
        the database instance still exists and attempts to roll back to it,
        causing the update rollback to fail.

        :param stack_name: The name or the unique ID of the stack that you want to continue rolling
        back.
        :param role_arn: The Amazon Resource Name (ARN) of an Identity and Access Management
        (IAM) role that CloudFormation assumes to roll back the stack.
        :param resources_to_skip: A list of the logical IDs of the resources that CloudFormation skips
        during the continue update rollback operation.
        :param client_request_token: A unique identifier for this ``ContinueUpdateRollback`` request.
        :returns: ContinueUpdateRollbackOutput
        :raises TokenAlreadyExistsException:
        """
        raise NotImplementedError

    @handler("CreateChangeSet")
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
        """Creates a list of changes that will be applied to a stack so that you
        can review the changes before executing them. You can create a change
        set for a stack that doesn't exist or an existing stack. If you create a
        change set for a stack that doesn't exist, the change set shows all of
        the resources that CloudFormation will create. If you create a change
        set for an existing stack, CloudFormation compares the stack's
        information with the information that you submit in the change set and
        lists the differences. Use change sets to understand which resources
        CloudFormation will create or change, and how it will change resources
        in an existing stack, before you create or update a stack.

        To create a change set for a stack that doesn't exist, for the
        ``ChangeSetType`` parameter, specify ``CREATE``. To create a change set
        for an existing stack, specify ``UPDATE`` for the ``ChangeSetType``
        parameter. To create a change set for an import operation, specify
        ``IMPORT`` for the ``ChangeSetType`` parameter. After the
        ``CreateChangeSet`` call successfully completes, CloudFormation starts
        creating the change set. To check the status of the change set or to
        review it, use the DescribeChangeSet action.

        When you are satisfied with the changes the change set will make,
        execute the change set by using the ExecuteChangeSet action.
        CloudFormation doesn't make changes until you execute the change set.

        To create a change set for the entire stack hierarchy, set
        ``IncludeNestedStacks`` to ``True``.

        :param stack_name: The name or the unique ID of the stack for which you are creating a
        change set.
        :param change_set_name: The name of the change set.
        :param template_body: A structure that contains the body of the revised template, with a
        minimum length of 1 byte and a maximum length of 51,200 bytes.
        :param template_url: The location of the file that contains the revised template.
        :param use_previous_template: Whether to reuse the template that's associated with the stack to create
        the change set.
        :param parameters: A list of ``Parameter`` structures that specify input parameters for the
        change set.
        :param capabilities: In some cases, you must explicitly acknowledge that your stack template
        contains certain capabilities in order for CloudFormation to create the
        stack.
        :param resource_types: The template resource types that you have permissions to work with if
        you execute this change set, such as ``AWS::EC2::Instance``,
        ``AWS::EC2::*``, or ``Custom::MyCustomInstance``.
        :param role_arn: The Amazon Resource Name (ARN) of an Identity and Access Management
        (IAM) role that CloudFormation assumes when executing the change set.
        :param rollback_configuration: The rollback triggers for CloudFormation to monitor during stack
        creation and updating operations, and for the specified monitoring
        period afterwards.
        :param notification_arns: The Amazon Resource Names (ARNs) of Amazon Simple Notification Service
        (Amazon SNS) topics that CloudFormation associates with the stack.
        :param tags: Key-value pairs to associate with this stack.
        :param client_token: A unique identifier for this ``CreateChangeSet`` request.
        :param description: A description to help you identify this change set.
        :param change_set_type: The type of change set operation.
        :param resources_to_import: The resources to import into your stack.
        :param include_nested_stacks: Creates a change set for the all nested stacks specified in the
        template.
        :returns: CreateChangeSetOutput
        :raises AlreadyExistsException:
        :raises InsufficientCapabilitiesException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateStack")
    def create_stack(
        self,
        context: RequestContext,
        stack_name: StackName,
        template_body: TemplateBody = None,
        template_url: TemplateURL = None,
        parameters: Parameters = None,
        disable_rollback: DisableRollback = None,
        rollback_configuration: RollbackConfiguration = None,
        timeout_in_minutes: TimeoutMinutes = None,
        notification_arns: NotificationARNs = None,
        capabilities: Capabilities = None,
        resource_types: ResourceTypes = None,
        role_arn: RoleARN = None,
        on_failure: OnFailure = None,
        stack_policy_body: StackPolicyBody = None,
        stack_policy_url: StackPolicyURL = None,
        tags: Tags = None,
        client_request_token: ClientRequestToken = None,
        enable_termination_protection: EnableTerminationProtection = None,
    ) -> CreateStackOutput:
        """Creates a stack as specified in the template. After the call completes
        successfully, the stack creation starts. You can check the status of the
        stack through the DescribeStacksoperation.

        :param stack_name: The name that's associated with the stack.
        :param template_body: Structure containing the template body with a minimum length of 1 byte
        and a maximum length of 51,200 bytes.
        :param template_url: Location of file containing the template body.
        :param parameters: A list of ``Parameter`` structures that specify input parameters for the
        stack.
        :param disable_rollback: Set to ``true`` to disable rollback of the stack if stack creation
        failed.
        :param rollback_configuration: The rollback triggers for CloudFormation to monitor during stack
        creation and updating operations, and for the specified monitoring
        period afterwards.
        :param timeout_in_minutes: The amount of time that can pass before the stack status becomes
        CREATE_FAILED; if ``DisableRollback`` is not set or is set to ``false``,
        the stack will be rolled back.
        :param notification_arns: The Amazon Simple Notification Service (Amazon SNS) topic ARNs to
        publish stack related events.
        :param capabilities: In some cases, you must explicitly acknowledge that your stack template
        contains certain capabilities in order for CloudFormation to create the
        stack.
        :param resource_types: The template resource types that you have permissions to work with for
        this create stack action, such as ``AWS::EC2::Instance``,
        ``AWS::EC2::*``, or ``Custom::MyCustomInstance``.
        :param role_arn: The Amazon Resource Name (ARN) of an Identity and Access Management
        (IAM) role that CloudFormation assumes to create the stack.
        :param on_failure: Determines what action will be taken if stack creation fails.
        :param stack_policy_body: Structure containing the stack policy body.
        :param stack_policy_url: Location of a file containing the stack policy.
        :param tags: Key-value pairs to associate with this stack.
        :param client_request_token: A unique identifier for this ``CreateStack`` request.
        :param enable_termination_protection: Whether to enable termination protection on the specified stack.
        :returns: CreateStackOutput
        :raises LimitExceededException:
        :raises AlreadyExistsException:
        :raises TokenAlreadyExistsException:
        :raises InsufficientCapabilitiesException:
        """
        raise NotImplementedError

    @handler("CreateStackInstances")
    def create_stack_instances(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        regions: RegionList,
        accounts: AccountList = None,
        deployment_targets: DeploymentTargets = None,
        parameter_overrides: Parameters = None,
        operation_preferences: StackSetOperationPreferences = None,
        operation_id: ClientRequestToken = None,
        call_as: CallAs = None,
    ) -> CreateStackInstancesOutput:
        """Creates stack instances for the specified accounts, within the specified
        Amazon Web Services Regions. A stack instance refers to a stack in a
        specific account and Region. You must specify at least one value for
        either ``Accounts`` or ``DeploymentTargets``, and you must specify at
        least one value for ``Regions``.

        :param stack_set_name: The name or unique ID of the stack set that you want to create stack
        instances from.
        :param regions: The names of one or more Amazon Web Services Regions where you want to
        create stack instances using the specified Amazon Web Services accounts.
        :param accounts: [Self-managed permissions] The names of one or more Amazon Web Services
        accounts that you want to create stack instances in the specified
        Region(s) for.
        :param deployment_targets: [Service-managed permissions] The Organizations accounts for which to
        create stack instances in the specified Amazon Web Services Regions.
        :param parameter_overrides: A list of stack set parameters whose values you want to override in the
        selected stack instances.
        :param operation_preferences: Preferences for how CloudFormation performs this stack set operation.
        :param operation_id: The unique identifier for this stack set operation.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: CreateStackInstancesOutput
        :raises StackSetNotFoundException:
        :raises OperationInProgressException:
        :raises OperationIdAlreadyExistsException:
        :raises StaleRequestException:
        :raises InvalidOperationException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("CreateStackSet")
    def create_stack_set(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        description: Description = None,
        template_body: TemplateBody = None,
        template_url: TemplateURL = None,
        stack_id: StackId = None,
        parameters: Parameters = None,
        capabilities: Capabilities = None,
        tags: Tags = None,
        administration_role_arn: RoleARN = None,
        execution_role_name: ExecutionRoleName = None,
        permission_model: PermissionModels = None,
        auto_deployment: AutoDeployment = None,
        call_as: CallAs = None,
        client_request_token: ClientRequestToken = None,
        managed_execution: ManagedExecution = None,
    ) -> CreateStackSetOutput:
        """Creates a stack set.

        :param stack_set_name: The name to associate with the stack set.
        :param description: A description of the stack set.
        :param template_body: The structure that contains the template body, with a minimum length of
        1 byte and a maximum length of 51,200 bytes.
        :param template_url: The location of the file that contains the template body.
        :param stack_id: The stack ID you are importing into a new stack set.
        :param parameters: The input parameters for the stack set template.
        :param capabilities: In some cases, you must explicitly acknowledge that your stack set
        template contains certain capabilities in order for CloudFormation to
        create the stack set and related stack instances.
        :param tags: The key-value pairs to associate with this stack set and the stacks
        created from it.
        :param administration_role_arn: The Amazon Resource Number (ARN) of the IAM role to use to create this
        stack set.
        :param execution_role_name: The name of the IAM execution role to use to create the stack set.
        :param permission_model: Describes how the IAM roles required for stack set operations are
        created.
        :param auto_deployment: Describes whether StackSets automatically deploys to Organizations
        accounts that are added to the target organization or organizational
        unit (OU).
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :param client_request_token: A unique identifier for this ``CreateStackSet`` request.
        :param managed_execution: Describes whether StackSets performs non-conflicting operations
        concurrently and queues conflicting operations.
        :returns: CreateStackSetOutput
        :raises NameAlreadyExistsException:
        :raises CreatedButModifiedException:
        :raises LimitExceededException:
        """
        raise NotImplementedError

    @handler("DeactivateType", expand=False)
    def deactivate_type(
        self, context: RequestContext, request: DeactivateTypeInput
    ) -> DeactivateTypeOutput:
        """Deactivates a public extension that was previously activated in this
        account and region.

        Once deactivated, an extension can't be used in any CloudFormation
        operation. This includes stack update operations where the stack
        template includes the extension, even if no updates are being made to
        the extension. In addition, deactivated extensions aren't automatically
        updated if a new version of the extension is released.

        :param type_name: The type name of the extension, in this account and region.
        :param type: The extension type.
        :param arn: The Amazon Resource Name (ARN) for the extension, in this account and
        region.
        :returns: DeactivateTypeOutput
        :raises CFNRegistryException:
        :raises TypeNotFoundException:
        """
        raise NotImplementedError

    @handler("DeleteChangeSet")
    def delete_change_set(
        self,
        context: RequestContext,
        change_set_name: ChangeSetNameOrId,
        stack_name: StackNameOrId = None,
    ) -> DeleteChangeSetOutput:
        """Deletes the specified change set. Deleting change sets ensures that no
        one executes the wrong change set.

        If the call successfully completes, CloudFormation successfully deleted
        the change set.

        If ``IncludeNestedStacks`` specifies ``True`` during the creation of the
        nested change set, then ``DeleteChangeSet`` will delete all change sets
        that belong to the stacks hierarchy and will also delete all change sets
        for nested stacks with the status of ``REVIEW_IN_PROGRESS``.

        :param change_set_name: The name or Amazon Resource Name (ARN) of the change set that you want
        to delete.
        :param stack_name: If you specified the name of a change set to delete, specify the stack
        name or Amazon Resource Name (ARN) that's associated with it.
        :returns: DeleteChangeSetOutput
        :raises InvalidChangeSetStatusException:
        """
        raise NotImplementedError

    @handler("DeleteStack")
    def delete_stack(
        self,
        context: RequestContext,
        stack_name: StackName,
        retain_resources: RetainResources = None,
        role_arn: RoleARN = None,
        client_request_token: ClientRequestToken = None,
    ) -> None:
        """Deletes a specified stack. Once the call completes successfully, stack
        deletion starts. Deleted stacks don't show up in the DescribeStacks
        operation if the deletion has been completed successfully.

        :param stack_name: The name or the unique stack ID that's associated with the stack.
        :param retain_resources: For stacks in the ``DELETE_FAILED`` state, a list of resource logical
        IDs that are associated with the resources you want to retain.
        :param role_arn: The Amazon Resource Name (ARN) of an Identity and Access Management
        (IAM) role that CloudFormation assumes to delete the stack.
        :param client_request_token: A unique identifier for this ``DeleteStack`` request.
        :raises TokenAlreadyExistsException:
        """
        raise NotImplementedError

    @handler("DeleteStackInstances")
    def delete_stack_instances(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        regions: RegionList,
        retain_stacks: RetainStacks,
        accounts: AccountList = None,
        deployment_targets: DeploymentTargets = None,
        operation_preferences: StackSetOperationPreferences = None,
        operation_id: ClientRequestToken = None,
        call_as: CallAs = None,
    ) -> DeleteStackInstancesOutput:
        """Deletes stack instances for the specified accounts, in the specified
        Amazon Web Services Regions.

        :param stack_set_name: The name or unique ID of the stack set that you want to delete stack
        instances for.
        :param regions: The Amazon Web Services Regions where you want to delete stack set
        instances.
        :param retain_stacks: Removes the stack instances from the specified stack set, but doesn't
        delete the stacks.
        :param accounts: [Self-managed permissions] The names of the Amazon Web Services accounts
        that you want to delete stack instances for.
        :param deployment_targets: [Service-managed permissions] The Organizations accounts from which to
        delete stack instances.
        :param operation_preferences: Preferences for how CloudFormation performs this stack set operation.
        :param operation_id: The unique identifier for this stack set operation.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: DeleteStackInstancesOutput
        :raises StackSetNotFoundException:
        :raises OperationInProgressException:
        :raises OperationIdAlreadyExistsException:
        :raises StaleRequestException:
        :raises InvalidOperationException:
        """
        raise NotImplementedError

    @handler("DeleteStackSet")
    def delete_stack_set(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        call_as: CallAs = None,
    ) -> DeleteStackSetOutput:
        """Deletes a stack set. Before you can delete a stack set, all of its
        member stack instances must be deleted. For more information about how
        to do this, see DeleteStackInstances.

        :param stack_set_name: The name or unique ID of the stack set that you're deleting.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: DeleteStackSetOutput
        :raises StackSetNotEmptyException:
        :raises OperationInProgressException:
        """
        raise NotImplementedError

    @handler("DeregisterType", expand=False)
    def deregister_type(
        self, context: RequestContext, request: DeregisterTypeInput
    ) -> DeregisterTypeOutput:
        """Marks an extension or extension version as ``DEPRECATED`` in the
        CloudFormation registry, removing it from active use. Deprecated
        extensions or extension versions cannot be used in CloudFormation
        operations.

        To deregister an entire extension, you must individually deregister all
        active versions of that extension. If an extension has only a single
        active version, deregistering that version results in the extension
        itself being deregistered and marked as deprecated in the registry.

        You can't deregister the default version of an extension if there are
        other active version of that extension. If you do deregister the default
        version of an extension, the extension type itself is deregistered as
        well and marked as deprecated.

        To view the deprecation status of an extension or extension version, use
        `DescribeType <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html>`__.

        :param arn: The Amazon Resource Name (ARN) of the extension.
        :param type: The kind of extension.
        :param type_name: The name of the extension.
        :param version_id: The ID of a specific version of the extension.
        :returns: DeregisterTypeOutput
        :raises CFNRegistryException:
        :raises TypeNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeAccountLimits")
    def describe_account_limits(
        self, context: RequestContext, next_token: NextToken = None
    ) -> DescribeAccountLimitsOutput:
        """Retrieves your account's CloudFormation limits, such as the maximum
        number of stacks that you can create in your account. For more
        information about account limits, see `CloudFormation
        Quotas <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html>`__
        in the *CloudFormation User Guide*.

        :param next_token: A string that identifies the next page of limits that you want to
        retrieve.
        :returns: DescribeAccountLimitsOutput
        """
        raise NotImplementedError

    @handler("DescribeChangeSet")
    def describe_change_set(
        self,
        context: RequestContext,
        change_set_name: ChangeSetNameOrId,
        stack_name: StackNameOrId = None,
        next_token: NextToken = None,
    ) -> DescribeChangeSetOutput:
        """Returns the inputs for the change set and a list of changes that
        CloudFormation will make if you execute the change set. For more
        information, see `Updating Stacks Using Change
        Sets <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html>`__
        in the CloudFormation User Guide.

        :param change_set_name: The name or Amazon Resource Name (ARN) of the change set that you want
        to describe.
        :param stack_name: If you specified the name of a change set, specify the stack name or ID
        (ARN) of the change set you want to describe.
        :param next_token: A string (provided by the DescribeChangeSet response output) that
        identifies the next page of information that you want to retrieve.
        :returns: DescribeChangeSetOutput
        :raises ChangeSetNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeChangeSetHooks")
    def describe_change_set_hooks(
        self,
        context: RequestContext,
        change_set_name: ChangeSetNameOrId,
        stack_name: StackNameOrId = None,
        next_token: NextToken = None,
        logical_resource_id: LogicalResourceId = None,
    ) -> DescribeChangeSetHooksOutput:
        """Returns hook-related information for the change set and a list of
        changes that CloudFormation makes when you run the change set.

        :param change_set_name: The name or Amazon Resource Name (ARN) of the change set that you want
        to describe.
        :param stack_name: If you specified the name of a change set, specify the stack name or
        stack ID (ARN) of the change set you want to describe.
        :param next_token: A string, provided by the ``DescribeChangeSetHooks`` response output,
        that identifies the next page of information that you want to retrieve.
        :param logical_resource_id: If specified, lists only the hooks related to the specified
        ``LogicalResourceId``.
        :returns: DescribeChangeSetHooksOutput
        :raises ChangeSetNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribePublisher")
    def describe_publisher(
        self, context: RequestContext, publisher_id: PublisherId = None
    ) -> DescribePublisherOutput:
        """Returns information about a CloudFormation extension publisher.

        If you don't supply a ``PublisherId``, and you have registered as an
        extension publisher, ``DescribePublisher`` returns information about
        your own publisher account.

        For more information on registering as a publisher, see:

        -  `RegisterPublisher <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html>`__

        -  `Publishing extensions to make them available for public
           use <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html>`__
           in the *CloudFormation CLI User Guide*

        :param publisher_id: The ID of the extension publisher.
        :returns: DescribePublisherOutput
        :raises CFNRegistryException:
        """
        raise NotImplementedError

    @handler("DescribeStackDriftDetectionStatus")
    def describe_stack_drift_detection_status(
        self, context: RequestContext, stack_drift_detection_id: StackDriftDetectionId
    ) -> DescribeStackDriftDetectionStatusOutput:
        """Returns information about a stack drift detection operation. A stack
        drift detection operation detects whether a stack's actual configuration
        differs, or has *drifted*, from it's expected configuration, as defined
        in the stack template and any values specified as template parameters. A
        stack is considered to have drifted if one or more of its resources have
        drifted. For more information on stack and resource drift, see
        `Detecting Unregulated Configuration Changes to Stacks and
        Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__.

        Use DetectStackDrift to initiate a stack drift detection operation.
        ``DetectStackDrift`` returns a ``StackDriftDetectionId`` you can use to
        monitor the progress of the operation using
        ``DescribeStackDriftDetectionStatus``. Once the drift detection
        operation has completed, use DescribeStackResourceDrifts to return drift
        information about the stack and its resources.

        :param stack_drift_detection_id: The ID of the drift detection results of this operation.
        :returns: DescribeStackDriftDetectionStatusOutput
        """
        raise NotImplementedError

    @handler("DescribeStackEvents")
    def describe_stack_events(
        self,
        context: RequestContext,
        stack_name: StackName = None,
        next_token: NextToken = None,
    ) -> DescribeStackEventsOutput:
        """Returns all stack related events for a specified stack in reverse
        chronological order. For more information about a stack's event history,
        go to
        `Stacks <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html>`__
        in the CloudFormation User Guide.

        You can list events for stacks that have failed to create or have been
        deleted by specifying the unique stack identifier (stack ID).

        :param stack_name: The name or the unique stack ID that's associated with the stack, which
        aren't always interchangeable:

        -  Running stacks: You can specify either the stack's name or its unique
           stack ID.
        :param next_token: A string that identifies the next page of events that you want to
        retrieve.
        :returns: DescribeStackEventsOutput
        """
        raise NotImplementedError

    @handler("DescribeStackInstance")
    def describe_stack_instance(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        stack_instance_account: Account,
        stack_instance_region: Region,
        call_as: CallAs = None,
    ) -> DescribeStackInstanceOutput:
        """Returns the stack instance that's associated with the specified stack
        set, Amazon Web Services account, and Region.

        For a list of stack instances that are associated with a specific stack
        set, use ListStackInstances.

        :param stack_set_name: The name or the unique stack ID of the stack set that you want to get
        stack instance information for.
        :param stack_instance_account: The ID of an Amazon Web Services account that's associated with this
        stack instance.
        :param stack_instance_region: The name of a Region that's associated with this stack instance.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: DescribeStackInstanceOutput
        :raises StackSetNotFoundException:
        :raises StackInstanceNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeStackResource")
    def describe_stack_resource(
        self,
        context: RequestContext,
        stack_name: StackName,
        logical_resource_id: LogicalResourceId,
    ) -> DescribeStackResourceOutput:
        """Returns a description of the specified resource in the specified stack.

        For deleted stacks, DescribeStackResource returns resource information
        for up to 90 days after the stack has been deleted.

        :param stack_name: The name or the unique stack ID that's associated with the stack, which
        aren't always interchangeable:

        -  Running stacks: You can specify either the stack's name or its unique
           stack ID.
        :param logical_resource_id: The logical name of the resource as specified in the template.
        :returns: DescribeStackResourceOutput
        """
        raise NotImplementedError

    @handler("DescribeStackResourceDrifts")
    def describe_stack_resource_drifts(
        self,
        context: RequestContext,
        stack_name: StackNameOrId,
        stack_resource_drift_status_filters: StackResourceDriftStatusFilters = None,
        next_token: NextToken = None,
        max_results: BoxedMaxResults = None,
    ) -> DescribeStackResourceDriftsOutput:
        """Returns drift information for the resources that have been checked for
        drift in the specified stack. This includes actual and expected
        configuration values for resources where CloudFormation detects
        configuration drift.

        For a given stack, there will be one ``StackResourceDrift`` for each
        stack resource that has been checked for drift. Resources that haven't
        yet been checked for drift aren't included. Resources that don't
        currently support drift detection aren't checked, and so not included.
        For a list of resources that support drift detection, see `Resources
        that Support Drift
        Detection <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__.

        Use DetectStackResourceDrift to detect drift on individual resources, or
        DetectStackDrift to detect drift on all supported resources for a given
        stack.

        :param stack_name: The name of the stack for which you want drift information.
        :param stack_resource_drift_status_filters: The resource drift status values to use as filters for the resource
        drift results returned.
        :param next_token: A string that identifies the next page of stack resource drift results.
        :param max_results: The maximum number of results to be returned with a single call.
        :returns: DescribeStackResourceDriftsOutput
        """
        raise NotImplementedError

    @handler("DescribeStackResources")
    def describe_stack_resources(
        self,
        context: RequestContext,
        stack_name: StackName = None,
        logical_resource_id: LogicalResourceId = None,
        physical_resource_id: PhysicalResourceId = None,
    ) -> DescribeStackResourcesOutput:
        """Returns Amazon Web Services resource descriptions for running and
        deleted stacks. If ``StackName`` is specified, all the associated
        resources that are part of the stack are returned. If
        ``PhysicalResourceId`` is specified, the associated resources of the
        stack that the resource belongs to are returned.

        Only the first 100 resources will be returned. If your stack has more
        resources than this, you should use ``ListStackResources`` instead.

        For deleted stacks, ``DescribeStackResources`` returns resource
        information for up to 90 days after the stack has been deleted.

        You must specify either ``StackName`` or ``PhysicalResourceId``, but not
        both. In addition, you can specify ``LogicalResourceId`` to filter the
        returned result. For more information about resources, the
        ``LogicalResourceId`` and ``PhysicalResourceId``, go to the
        `CloudFormation User
        Guide <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/>`__.

        A ``ValidationError`` is returned if you specify both ``StackName`` and
        ``PhysicalResourceId`` in the same request.

        :param stack_name: The name or the unique stack ID that is associated with the stack, which
        aren't always interchangeable:

        -  Running stacks: You can specify either the stack's name or its unique
           stack ID.
        :param logical_resource_id: The logical name of the resource as specified in the template.
        :param physical_resource_id: The name or unique identifier that corresponds to a physical instance ID
        of a resource supported by CloudFormation.
        :returns: DescribeStackResourcesOutput
        """
        raise NotImplementedError

    @handler("DescribeStackSet")
    def describe_stack_set(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        call_as: CallAs = None,
    ) -> DescribeStackSetOutput:
        """Returns the description of the specified stack set.

        :param stack_set_name: The name or unique ID of the stack set whose description you want.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: DescribeStackSetOutput
        :raises StackSetNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeStackSetOperation")
    def describe_stack_set_operation(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        operation_id: ClientRequestToken,
        call_as: CallAs = None,
    ) -> DescribeStackSetOperationOutput:
        """Returns the description of the specified stack set operation.

        :param stack_set_name: The name or the unique stack ID of the stack set for the stack
        operation.
        :param operation_id: The unique ID of the stack set operation.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: DescribeStackSetOperationOutput
        :raises StackSetNotFoundException:
        :raises OperationNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeStacks")
    def describe_stacks(
        self,
        context: RequestContext,
        stack_name: StackName = None,
        next_token: NextToken = None,
    ) -> DescribeStacksOutput:
        """Returns the description for the specified stack; if no stack name was
        specified, then it returns the description for all the stacks created.

        If the stack doesn't exist, an ``ValidationError`` is returned.

        :param stack_name: The name or the unique stack ID that's associated with the stack, which
        aren't always interchangeable:

        -  Running stacks: You can specify either the stack's name or its unique
           stack ID.
        :param next_token: A string that identifies the next page of stacks that you want to
        retrieve.
        :returns: DescribeStacksOutput
        """
        raise NotImplementedError

    @handler("DescribeType", expand=False)
    def describe_type(
        self, context: RequestContext, request: DescribeTypeInput
    ) -> DescribeTypeOutput:
        """Returns detailed information about an extension that has been
        registered.

        If you specify a ``VersionId``, ``DescribeType`` returns information
        about that specific extension version. Otherwise, it returns information
        about the default extension version.

        :param type: The kind of extension.
        :param type_name: The name of the extension.
        :param arn: The Amazon Resource Name (ARN) of the extension.
        :param version_id: The ID of a specific version of the extension.
        :param publisher_id: The publisher ID of the extension publisher.
        :param public_version_number: The version number of a public third-party extension.
        :returns: DescribeTypeOutput
        :raises CFNRegistryException:
        :raises TypeNotFoundException:
        """
        raise NotImplementedError

    @handler("DescribeTypeRegistration")
    def describe_type_registration(
        self, context: RequestContext, registration_token: RegistrationToken
    ) -> DescribeTypeRegistrationOutput:
        """Returns information about an extension's registration, including its
        current status and type and version identifiers.

        When you initiate a registration request using ``RegisterType``, you can
        then use ``DescribeTypeRegistration`` to monitor the progress of that
        registration request.

        Once the registration request has completed, use ``DescribeType`` to
        return detailed information about an extension.

        :param registration_token: The identifier for this registration request.
        :returns: DescribeTypeRegistrationOutput
        :raises CFNRegistryException:
        """
        raise NotImplementedError

    @handler("DetectStackDrift")
    def detect_stack_drift(
        self,
        context: RequestContext,
        stack_name: StackNameOrId,
        logical_resource_ids: LogicalResourceIds = None,
    ) -> DetectStackDriftOutput:
        """Detects whether a stack's actual configuration differs, or has
        *drifted*, from it's expected configuration, as defined in the stack
        template and any values specified as template parameters. For each
        resource in the stack that supports drift detection, CloudFormation
        compares the actual configuration of the resource with its expected
        template configuration. Only resource properties explicitly defined in
        the stack template are checked for drift. A stack is considered to have
        drifted if one or more of its resources differ from their expected
        template configurations. For more information, see `Detecting
        Unregulated Configuration Changes to Stacks and
        Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__.

        Use ``DetectStackDrift`` to detect drift on all supported resources for
        a given stack, or DetectStackResourceDrift to detect drift on individual
        resources.

        For a list of stack resources that currently support drift detection,
        see `Resources that Support Drift
        Detection <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__.

        ``DetectStackDrift`` can take up to several minutes, depending on the
        number of resources contained within the stack. Use
        DescribeStackDriftDetectionStatus to monitor the progress of a detect
        stack drift operation. Once the drift detection operation has completed,
        use DescribeStackResourceDrifts to return drift information about the
        stack and its resources.

        When detecting drift on a stack, CloudFormation doesn't detect drift on
        any nested stacks belonging to that stack. Perform ``DetectStackDrift``
        directly on the nested stack itself.

        :param stack_name: The name of the stack for which you want to detect drift.
        :param logical_resource_ids: The logical names of any resources you want to use as filters.
        :returns: DetectStackDriftOutput
        """
        raise NotImplementedError

    @handler("DetectStackResourceDrift")
    def detect_stack_resource_drift(
        self,
        context: RequestContext,
        stack_name: StackNameOrId,
        logical_resource_id: LogicalResourceId,
    ) -> DetectStackResourceDriftOutput:
        """Returns information about whether a resource's actual configuration
        differs, or has *drifted*, from it's expected configuration, as defined
        in the stack template and any values specified as template parameters.
        This information includes actual and expected property values for
        resources in which CloudFormation detects drift. Only resource
        properties explicitly defined in the stack template are checked for
        drift. For more information about stack and resource drift, see
        `Detecting Unregulated Configuration Changes to Stacks and
        Resources <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html>`__.

        Use ``DetectStackResourceDrift`` to detect drift on individual
        resources, or DetectStackDrift to detect drift on all resources in a
        given stack that support drift detection.

        Resources that don't currently support drift detection can't be checked.
        For a list of resources that support drift detection, see `Resources
        that Support Drift
        Detection <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html>`__.

        :param stack_name: The name of the stack to which the resource belongs.
        :param logical_resource_id: The logical name of the resource for which to return drift information.
        :returns: DetectStackResourceDriftOutput
        """
        raise NotImplementedError

    @handler("DetectStackSetDrift")
    def detect_stack_set_drift(
        self,
        context: RequestContext,
        stack_set_name: StackSetNameOrId,
        operation_preferences: StackSetOperationPreferences = None,
        operation_id: ClientRequestToken = None,
        call_as: CallAs = None,
    ) -> DetectStackSetDriftOutput:
        """Detect drift on a stack set. When CloudFormation performs drift
        detection on a stack set, it performs drift detection on the stack
        associated with each stack instance in the stack set. For more
        information, see `How CloudFormation performs drift detection on a stack
        set <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html>`__.

        ``DetectStackSetDrift`` returns the ``OperationId`` of the stack set
        drift detection operation. Use this operation id with
        ``DescribeStackSetOperation`` to monitor the progress of the drift
        detection operation. The drift detection operation may take some time,
        depending on the number of stack instances included in the stack set, in
        addition to the number of resources included in each stack.

        Once the operation has completed, use the following actions to return
        drift information:

        -  Use ``DescribeStackSet`` to return detailed information about the
           stack set, including detailed information about the last *completed*
           drift operation performed on the stack set. (Information about drift
           operations that are in progress isn't included.)

        -  Use ``ListStackInstances`` to return a list of stack instances
           belonging to the stack set, including the drift status and last drift
           time checked of each instance.

        -  Use ``DescribeStackInstance`` to return detailed information about a
           specific stack instance, including its drift status and last drift
           time checked.

        For more information on performing a drift detection operation on a
        stack set, see `Detecting unmanaged changes in stack
        sets <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html>`__.

        You can only run a single drift detection operation on a given stack set
        at one time.

        To stop a drift detection stack set operation, use
        ``StopStackSetOperation``.

        :param stack_set_name: The name of the stack set on which to perform the drift detection
        operation.
        :param operation_preferences: The user-specified preferences for how CloudFormation performs a stack
        set operation.
        :param operation_id: *The ID of the stack set operation.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: DetectStackSetDriftOutput
        :raises InvalidOperationException:
        :raises OperationInProgressException:
        :raises StackSetNotFoundException:
        """
        raise NotImplementedError

    @handler("EstimateTemplateCost")
    def estimate_template_cost(
        self,
        context: RequestContext,
        template_body: TemplateBody = None,
        template_url: TemplateURL = None,
        parameters: Parameters = None,
    ) -> EstimateTemplateCostOutput:
        """Returns the estimated monthly cost of a template. The return value is an
        Amazon Web Services Simple Monthly Calculator URL with a query string
        that describes the resources required to run the template.

        :param template_body: Structure containing the template body with a minimum length of 1 byte
        and a maximum length of 51,200 bytes.
        :param template_url: Location of file containing the template body.
        :param parameters: A list of ``Parameter`` structures that specify input parameters.
        :returns: EstimateTemplateCostOutput
        """
        raise NotImplementedError

    @handler("ExecuteChangeSet")
    def execute_change_set(
        self,
        context: RequestContext,
        change_set_name: ChangeSetNameOrId,
        stack_name: StackNameOrId = None,
        client_request_token: ClientRequestToken = None,
        disable_rollback: DisableRollback = None,
    ) -> ExecuteChangeSetOutput:
        """Updates a stack using the input information that was provided when the
        specified change set was created. After the call successfully completes,
        CloudFormation starts updating the stack. Use the DescribeStacks action
        to view the status of the update.

        When you execute a change set, CloudFormation deletes all other change
        sets associated with the stack because they aren't valid for the updated
        stack.

        If a stack policy is associated with the stack, CloudFormation enforces
        the policy during the update. You can't specify a temporary stack policy
        that overrides the current policy.

        To create a change set for the entire stack hierarchy,
        ``IncludeNestedStacks`` must have been set to ``True``.

        :param change_set_name: The name or Amazon Resource Name (ARN) of the change set that you want
        use to update the specified stack.
        :param stack_name: If you specified the name of a change set, specify the stack name or
        Amazon Resource Name (ARN) that's associated with the change set you
        want to execute.
        :param client_request_token: A unique identifier for this ``ExecuteChangeSet`` request.
        :param disable_rollback: Preserves the state of previously provisioned resources when an
        operation fails.
        :returns: ExecuteChangeSetOutput
        :raises InvalidChangeSetStatusException:
        :raises ChangeSetNotFoundException:
        :raises InsufficientCapabilitiesException:
        :raises TokenAlreadyExistsException:
        """
        raise NotImplementedError

    @handler("GetStackPolicy")
    def get_stack_policy(
        self, context: RequestContext, stack_name: StackName
    ) -> GetStackPolicyOutput:
        """Returns the stack policy for a specified stack. If a stack doesn't have
        a policy, a null value is returned.

        :param stack_name: The name or unique stack ID that's associated with the stack whose
        policy you want to get.
        :returns: GetStackPolicyOutput
        """
        raise NotImplementedError

    @handler("GetTemplate")
    def get_template(
        self,
        context: RequestContext,
        stack_name: StackName = None,
        change_set_name: ChangeSetNameOrId = None,
        template_stage: TemplateStage = None,
    ) -> GetTemplateOutput:
        """Returns the template body for a specified stack. You can get the
        template for running or deleted stacks.

        For deleted stacks, ``GetTemplate`` returns the template for up to 90
        days after the stack has been deleted.

        If the template doesn't exist, a ``ValidationError`` is returned.

        :param stack_name: The name or the unique stack ID that's associated with the stack, which
        aren't always interchangeable:

        -  Running stacks: You can specify either the stack's name or its unique
           stack ID.
        :param change_set_name: The name or Amazon Resource Name (ARN) of a change set for which
        CloudFormation returns the associated template.
        :param template_stage: For templates that include transforms, the stage of the template that
        CloudFormation returns.
        :returns: GetTemplateOutput
        :raises ChangeSetNotFoundException:
        """
        raise NotImplementedError

    @handler("GetTemplateSummary")
    def get_template_summary(
        self,
        context: RequestContext,
        template_body: TemplateBody = None,
        template_url: TemplateURL = None,
        stack_name: StackNameOrId = None,
        stack_set_name: StackSetNameOrId = None,
        call_as: CallAs = None,
    ) -> GetTemplateSummaryOutput:
        """Returns information about a new or existing template. The
        ``GetTemplateSummary`` action is useful for viewing parameter
        information, such as default parameter values and parameter types,
        before you create or update a stack or stack set.

        You can use the ``GetTemplateSummary`` action when you submit a
        template, or you can get template information for a stack set, or a
        running or deleted stack.

        For deleted stacks, ``GetTemplateSummary`` returns the template
        information for up to 90 days after the stack has been deleted. If the
        template doesn't exist, a ``ValidationError`` is returned.

        :param template_body: Structure containing the template body with a minimum length of 1 byte
        and a maximum length of 51,200 bytes.
        :param template_url: Location of file containing the template body.
        :param stack_name: The name or the stack ID that's associated with the stack, which aren't
        always interchangeable.
        :param stack_set_name: The name or unique ID of the stack set from which the stack was created.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: GetTemplateSummaryOutput
        :raises StackSetNotFoundException:
        """
        raise NotImplementedError

    @handler("ImportStacksToStackSet")
    def import_stacks_to_stack_set(
        self,
        context: RequestContext,
        stack_set_name: StackSetNameOrId,
        stack_ids: StackIdList = None,
        stack_ids_url: StackIdsUrl = None,
        organizational_unit_ids: OrganizationalUnitIdList = None,
        operation_preferences: StackSetOperationPreferences = None,
        operation_id: ClientRequestToken = None,
        call_as: CallAs = None,
    ) -> ImportStacksToStackSetOutput:
        """Import existing stacks into a new stack sets. Use the stack import
        operation to import up to 10 stacks into a new stack set in the same
        account as the source stack or in a different administrator account and
        Region, by specifying the stack ID of the stack you intend to import.

        ``ImportStacksToStackSet`` is only supported by self-managed
        permissions.

        :param stack_set_name: The name of the stack set.
        :param stack_ids: The IDs of the stacks you are importing into a stack set.
        :param stack_ids_url: The Amazon S3 URL which contains list of stack ids to be inputted.
        :param organizational_unit_ids: The list of OU ID's to which the stacks being imported has to be mapped
        as deployment target.
        :param operation_preferences: The user-specified preferences for how CloudFormation performs a stack
        set operation.
        :param operation_id: A unique, user defined, identifier for the stack set operation.
        :param call_as: By default, ``SELF`` is specified.
        :returns: ImportStacksToStackSetOutput
        :raises LimitExceededException:
        :raises StackSetNotFoundException:
        :raises InvalidOperationException:
        :raises OperationInProgressException:
        :raises OperationIdAlreadyExistsException:
        :raises StackNotFoundException:
        :raises StaleRequestException:
        """
        raise NotImplementedError

    @handler("ListChangeSets")
    def list_change_sets(
        self,
        context: RequestContext,
        stack_name: StackNameOrId,
        next_token: NextToken = None,
    ) -> ListChangeSetsOutput:
        """Returns the ID and status of each active change set for a stack. For
        example, CloudFormation lists change sets that are in the
        ``CREATE_IN_PROGRESS`` or ``CREATE_PENDING`` state.

        :param stack_name: The name or the Amazon Resource Name (ARN) of the stack for which you
        want to list change sets.
        :param next_token: A string (provided by the ListChangeSets response output) that
        identifies the next page of change sets that you want to retrieve.
        :returns: ListChangeSetsOutput
        """
        raise NotImplementedError

    @handler("ListExports")
    def list_exports(
        self, context: RequestContext, next_token: NextToken = None
    ) -> ListExportsOutput:
        """Lists all exported output values in the account and Region in which you
        call this action. Use this action to see the exported output values that
        you can import into other stacks. To import values, use the
        ```Fn::ImportValue`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html>`__
        function.

        For more information, see `CloudFormation export stack output
        values <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html>`__.

        :param next_token: A string (provided by the ListExports response output) that identifies
        the next page of exported output values that you asked to retrieve.
        :returns: ListExportsOutput
        """
        raise NotImplementedError

    @handler("ListImports")
    def list_imports(
        self,
        context: RequestContext,
        export_name: ExportName,
        next_token: NextToken = None,
    ) -> ListImportsOutput:
        """Lists all stacks that are importing an exported output value. To modify
        or remove an exported output value, first use this action to see which
        stacks are using it. To see the exported output values in your account,
        see ListExports.

        For more information about importing an exported output value, see the
        ```Fn::ImportValue`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html>`__
        function.

        :param export_name: The name of the exported output value.
        :param next_token: A string (provided by the ListImports response output) that identifies
        the next page of stacks that are importing the specified exported output
        value.
        :returns: ListImportsOutput
        """
        raise NotImplementedError

    @handler("ListStackInstances")
    def list_stack_instances(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        next_token: NextToken = None,
        max_results: MaxResults = None,
        filters: StackInstanceFilters = None,
        stack_instance_account: Account = None,
        stack_instance_region: Region = None,
        call_as: CallAs = None,
    ) -> ListStackInstancesOutput:
        """Returns summary information about stack instances that are associated
        with the specified stack set. You can filter for stack instances that
        are associated with a specific Amazon Web Services account name or
        Region, or that have a specific status.

        :param stack_set_name: The name or unique ID of the stack set that you want to list stack
        instances for.
        :param next_token: If the previous request didn't return all of the remaining results, the
        response's ``NextToken`` parameter value is set to a token.
        :param max_results: The maximum number of results to be returned with a single call.
        :param filters: The status that stack instances are filtered by.
        :param stack_instance_account: The name of the Amazon Web Services account that you want to list stack
        instances for.
        :param stack_instance_region: The name of the Region where you want to list stack instances.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: ListStackInstancesOutput
        :raises StackSetNotFoundException:
        """
        raise NotImplementedError

    @handler("ListStackResources")
    def list_stack_resources(
        self,
        context: RequestContext,
        stack_name: StackName,
        next_token: NextToken = None,
    ) -> ListStackResourcesOutput:
        """Returns descriptions of all resources of the specified stack.

        For deleted stacks, ListStackResources returns resource information for
        up to 90 days after the stack has been deleted.

        :param stack_name: The name or the unique stack ID that is associated with the stack, which
        aren't always interchangeable:

        -  Running stacks: You can specify either the stack's name or its unique
           stack ID.
        :param next_token: A string that identifies the next page of stack resources that you want
        to retrieve.
        :returns: ListStackResourcesOutput
        """
        raise NotImplementedError

    @handler("ListStackSetOperationResults")
    def list_stack_set_operation_results(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        operation_id: ClientRequestToken,
        next_token: NextToken = None,
        max_results: MaxResults = None,
        call_as: CallAs = None,
    ) -> ListStackSetOperationResultsOutput:
        """Returns summary information about the results of a stack set operation.

        :param stack_set_name: The name or unique ID of the stack set that you want to get operation
        results for.
        :param operation_id: The ID of the stack set operation.
        :param next_token: If the previous request didn't return all of the remaining results, the
        response object's ``NextToken`` parameter value is set to a token.
        :param max_results: The maximum number of results to be returned with a single call.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: ListStackSetOperationResultsOutput
        :raises StackSetNotFoundException:
        :raises OperationNotFoundException:
        """
        raise NotImplementedError

    @handler("ListStackSetOperations")
    def list_stack_set_operations(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        next_token: NextToken = None,
        max_results: MaxResults = None,
        call_as: CallAs = None,
    ) -> ListStackSetOperationsOutput:
        """Returns summary information about operations performed on a stack set.

        :param stack_set_name: The name or unique ID of the stack set that you want to get operation
        summaries for.
        :param next_token: If the previous paginated request didn't return all of the remaining
        results, the response object's ``NextToken`` parameter value is set to a
        token.
        :param max_results: The maximum number of results to be returned with a single call.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: ListStackSetOperationsOutput
        :raises StackSetNotFoundException:
        """
        raise NotImplementedError

    @handler("ListStackSets")
    def list_stack_sets(
        self,
        context: RequestContext,
        next_token: NextToken = None,
        max_results: MaxResults = None,
        status: StackSetStatus = None,
        call_as: CallAs = None,
    ) -> ListStackSetsOutput:
        """Returns summary information about stack sets that are associated with
        the user.

        -  [Self-managed permissions] If you set the ``CallAs`` parameter to
           ``SELF`` while signed in to your Amazon Web Services account,
           ``ListStackSets`` returns all self-managed stack sets in your Amazon
           Web Services account.

        -  [Service-managed permissions] If you set the ``CallAs`` parameter to
           ``SELF`` while signed in to the organization's management account,
           ``ListStackSets`` returns all stack sets in the management account.

        -  [Service-managed permissions] If you set the ``CallAs`` parameter to
           ``DELEGATED_ADMIN`` while signed in to your member account,
           ``ListStackSets`` returns all stack sets with service-managed
           permissions in the management account.

        :param next_token: If the previous paginated request didn't return all the remaining
        results, the response object's ``NextToken`` parameter value is set to a
        token.
        :param max_results: The maximum number of results to be returned with a single call.
        :param status: The status of the stack sets that you want to get summary information
        about.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the management account or as a delegated
        administrator in a member account.
        :returns: ListStackSetsOutput
        """
        raise NotImplementedError

    @handler("ListStacks")
    def list_stacks(
        self,
        context: RequestContext,
        next_token: NextToken = None,
        stack_status_filter: StackStatusFilter = None,
    ) -> ListStacksOutput:
        """Returns the summary information for stacks whose status matches the
        specified StackStatusFilter. Summary information for stacks that have
        been deleted is kept for 90 days after the stack is deleted. If no
        StackStatusFilter is specified, summary information for all stacks is
        returned (including existing stacks and stacks that have been deleted).

        :param next_token: A string that identifies the next page of stacks that you want to
        retrieve.
        :param stack_status_filter: Stack status to use as a filter.
        :returns: ListStacksOutput
        """
        raise NotImplementedError

    @handler("ListTypeRegistrations", expand=False)
    def list_type_registrations(
        self, context: RequestContext, request: ListTypeRegistrationsInput
    ) -> ListTypeRegistrationsOutput:
        """Returns a list of registration tokens for the specified extension(s).

        :param type: The kind of extension.
        :param type_name: The name of the extension.
        :param type_arn: The Amazon Resource Name (ARN) of the extension.
        :param registration_status_filter: The current status of the extension registration request.
        :param max_results: The maximum number of results to be returned with a single call.
        :param next_token: If the previous paginated request didn't return all the remaining
        results, the response object's ``NextToken`` parameter value is set to a
        token.
        :returns: ListTypeRegistrationsOutput
        :raises CFNRegistryException:
        """
        raise NotImplementedError

    @handler("ListTypeVersions", expand=False)
    def list_type_versions(
        self, context: RequestContext, request: ListTypeVersionsInput
    ) -> ListTypeVersionsOutput:
        """Returns summary information about the versions of an extension.

        :param type: The kind of the extension.
        :param type_name: The name of the extension for which you want version summary
        information.
        :param arn: The Amazon Resource Name (ARN) of the extension for which you want
        version summary information.
        :param max_results: The maximum number of results to be returned with a single call.
        :param next_token: If the previous paginated request didn't return all of the remaining
        results, the response object's ``NextToken`` parameter value is set to a
        token.
        :param deprecated_status: The deprecation status of the extension versions that you want to get
        summary information about.
        :param publisher_id: The publisher ID of the extension publisher.
        :returns: ListTypeVersionsOutput
        :raises CFNRegistryException:
        """
        raise NotImplementedError

    @handler("ListTypes", expand=False)
    def list_types(
        self, context: RequestContext, request: ListTypesInput
    ) -> ListTypesOutput:
        """Returns summary information about extension that have been registered
        with CloudFormation.

        :param visibility: The scope at which the extensions are visible and usable in
        CloudFormation operations.
        :param provisioning_type: For resource types, the provisioning behavior of the resource type.
        :param deprecated_status: The deprecation status of the extension that you want to get summary
        information about.
        :param type: The type of extension.
        :param filters: Filter criteria to use in determining which extensions to return.
        :param max_results: The maximum number of results to be returned with a single call.
        :param next_token: If the previous paginated request didn't return all of the remaining
        results, the response object's ``NextToken`` parameter value is set to a
        token.
        :returns: ListTypesOutput
        :raises CFNRegistryException:
        """
        raise NotImplementedError

    @handler("PublishType", expand=False)
    def publish_type(
        self, context: RequestContext, request: PublishTypeInput
    ) -> PublishTypeOutput:
        """Publishes the specified extension to the CloudFormation registry as a
        public extension in this region. Public extensions are available for use
        by all CloudFormation users. For more information on publishing
        extensions, see `Publishing extensions to make them available for public
        use <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html>`__
        in the *CloudFormation CLI User Guide*.

        To publish an extension, you must be registered as a publisher with
        CloudFormation. For more information, see
        `RegisterPublisher <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html>`__.

        :param type: The type of the extension.
        :param arn: The Amazon Resource Number (ARN) of the extension.
        :param type_name: The name of the extension.
        :param public_version_number: The version number to assign to this version of the extension.
        :returns: PublishTypeOutput
        :raises CFNRegistryException:
        :raises TypeNotFoundException:
        """
        raise NotImplementedError

    @handler("RecordHandlerProgress")
    def record_handler_progress(
        self,
        context: RequestContext,
        bearer_token: ClientToken,
        operation_status: OperationStatus,
        current_operation_status: OperationStatus = None,
        status_message: StatusMessage = None,
        error_code: HandlerErrorCode = None,
        resource_model: ResourceModel = None,
        client_request_token: ClientRequestToken = None,
    ) -> RecordHandlerProgressOutput:
        """Reports progress of a resource handler to CloudFormation.

        Reserved for use by the `CloudFormation
        CLI <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html>`__.
        Don't use this API in your code.

        :param bearer_token: Reserved for use by the `CloudFormation
        CLI <https://docs.
        :param operation_status: Reserved for use by the `CloudFormation
        CLI <https://docs.
        :param current_operation_status: Reserved for use by the `CloudFormation
        CLI <https://docs.
        :param status_message: Reserved for use by the `CloudFormation
        CLI <https://docs.
        :param error_code: Reserved for use by the `CloudFormation
        CLI <https://docs.
        :param resource_model: Reserved for use by the `CloudFormation
        CLI <https://docs.
        :param client_request_token: Reserved for use by the `CloudFormation
        CLI <https://docs.
        :returns: RecordHandlerProgressOutput
        :raises InvalidStateTransitionException:
        :raises OperationStatusCheckFailedException:
        """
        raise NotImplementedError

    @handler("RegisterPublisher")
    def register_publisher(
        self,
        context: RequestContext,
        accept_terms_and_conditions: AcceptTermsAndConditions = None,
        connection_arn: ConnectionArn = None,
    ) -> RegisterPublisherOutput:
        """Registers your account as a publisher of public extensions in the
        CloudFormation registry. Public extensions are available for use by all
        CloudFormation users. This publisher ID applies to your account in all
        Amazon Web Services Regions.

        For information on requirements for registering as a public extension
        publisher, see `Registering your account to publish CloudFormation
        extensions <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs>`__
        in the *CloudFormation CLI User Guide*.

        :param accept_terms_and_conditions: Whether you accept the `Terms and
        Conditions <https://cloudformation-registry-documents.
        :param connection_arn: If you are using a Bitbucket or GitHub account for identity
        verification, the Amazon Resource Name (ARN) for your connection to that
        account.
        :returns: RegisterPublisherOutput
        :raises CFNRegistryException:
        """
        raise NotImplementedError

    @handler("RegisterType", expand=False)
    def register_type(
        self, context: RequestContext, request: RegisterTypeInput
    ) -> RegisterTypeOutput:
        """Registers an extension with the CloudFormation service. Registering an
        extension makes it available for use in CloudFormation templates in your
        Amazon Web Services account, and includes:

        -  Validating the extension schema.

        -  Determining which handlers, if any, have been specified for the
           extension.

        -  Making the extension available for use in your account.

        For more information on how to develop extensions and ready them for
        registration, see `Creating Resource
        Providers <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html>`__
        in the *CloudFormation CLI User Guide*.

        You can have a maximum of 50 resource extension versions registered at a
        time. This maximum is per account and per region. Use
        `DeregisterType <AWSCloudFormation/latest/APIReference/API_DeregisterType.html>`__
        to deregister specific extension versions if necessary.

        Once you have initiated a registration request using ``RegisterType``,
        you can use ``DescribeTypeRegistration`` to monitor the progress of the
        registration request.

        Once you have registered a private extension in your account and region,
        use
        `SetTypeConfiguration <AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html>`__
        to specify configuration properties for the extension. For more
        information, see `Configuring extensions at the account
        level <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration>`__
        in the *CloudFormation User Guide*.

        :param type_name: The name of the extension being registered.
        :param schema_handler_package: A URL to the S3 bucket containing the extension project package that
        contains the necessary files for the extension you want to register.
        :param type: The kind of extension.
        :param logging_config: Specifies logging configuration information for an extension.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the IAM role for CloudFormation to
        assume when invoking the extension.
        :param client_request_token: A unique identifier that acts as an idempotency key for this
        registration request.
        :returns: RegisterTypeOutput
        :raises CFNRegistryException:
        """
        raise NotImplementedError

    @handler("RollbackStack")
    def rollback_stack(
        self,
        context: RequestContext,
        stack_name: StackNameOrId,
        role_arn: RoleARN = None,
        client_request_token: ClientRequestToken = None,
    ) -> RollbackStackOutput:
        """When specifying ``RollbackStack``, you preserve the state of previously
        provisioned resources when an operation fails. You can check the status
        of the stack through the DescribeStacks operation.

        Rolls back the specified stack to the last known stable state from
        ``CREATE_FAILED`` or ``UPDATE_FAILED`` stack statuses.

        This operation will delete a stack if it doesn't contain a last known
        stable state. A last known stable state includes any status in a
        ``*_COMPLETE``. This includes the following stack statuses.

        -  ``CREATE_COMPLETE``

        -  ``UPDATE_COMPLETE``

        -  ``UPDATE_ROLLBACK_COMPLETE``

        -  ``IMPORT_COMPLETE``

        -  ``IMPORT_ROLLBACK_COMPLETE``

        :param stack_name: The name that's associated with the stack.
        :param role_arn: The Amazon Resource Name (ARN) of an Identity and Access Management role
        that CloudFormation assumes to rollback the stack.
        :param client_request_token: A unique identifier for this ``RollbackStack`` request.
        :returns: RollbackStackOutput
        :raises TokenAlreadyExistsException:
        """
        raise NotImplementedError

    @handler("SetStackPolicy")
    def set_stack_policy(
        self,
        context: RequestContext,
        stack_name: StackName,
        stack_policy_body: StackPolicyBody = None,
        stack_policy_url: StackPolicyURL = None,
    ) -> None:
        """Sets a stack policy for a specified stack.

        :param stack_name: The name or unique stack ID that you want to associate a policy with.
        :param stack_policy_body: Structure containing the stack policy body.
        :param stack_policy_url: Location of a file containing the stack policy.
        """
        raise NotImplementedError

    @handler("SetTypeConfiguration", expand=False)
    def set_type_configuration(
        self, context: RequestContext, request: SetTypeConfigurationInput
    ) -> SetTypeConfigurationOutput:
        """Specifies the configuration data for a registered CloudFormation
        extension, in the given account and region.

        To view the current configuration data for an extension, refer to the
        ``ConfigurationSchema`` element of
        `DescribeType <AWSCloudFormation/latest/APIReference/API_DescribeType.html>`__.
        For more information, see `Configuring extensions at the account
        level <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration>`__
        in the *CloudFormation User Guide*.

        It's strongly recommended that you use dynamic references to restrict
        sensitive configuration definitions, such as third-party credentials.
        For more details on dynamic references, see `Using dynamic references to
        specify template values <https://docs.aws.amazon.com/>`__ in the
        *CloudFormation User Guide*.

        :param configuration: The configuration data for the extension, in this account and region.
        :param type_arn: The Amazon Resource Name (ARN) for the extension, in this account and
        region.
        :param configuration_alias: An alias by which to refer to this extension configuration data.
        :param type_name: The name of the extension.
        :param type: The type of extension.
        :returns: SetTypeConfigurationOutput
        :raises CFNRegistryException:
        :raises TypeNotFoundException:
        """
        raise NotImplementedError

    @handler("SetTypeDefaultVersion", expand=False)
    def set_type_default_version(
        self, context: RequestContext, request: SetTypeDefaultVersionInput
    ) -> SetTypeDefaultVersionOutput:
        """Specify the default version of an extension. The default version of an
        extension will be used in CloudFormation operations.

        :param arn: The Amazon Resource Name (ARN) of the extension for which you want
        version summary information.
        :param type: The kind of extension.
        :param type_name: The name of the extension.
        :param version_id: The ID of a specific version of the extension.
        :returns: SetTypeDefaultVersionOutput
        :raises CFNRegistryException:
        :raises TypeNotFoundException:
        """
        raise NotImplementedError

    @handler("SignalResource")
    def signal_resource(
        self,
        context: RequestContext,
        stack_name: StackNameOrId,
        logical_resource_id: LogicalResourceId,
        unique_id: ResourceSignalUniqueId,
        status: ResourceSignalStatus,
    ) -> None:
        """Sends a signal to the specified resource with a success or failure
        status. You can use the ``SignalResource`` operation in conjunction with
        a creation policy or update policy. CloudFormation doesn't proceed with
        a stack creation or update until resources receive the required number
        of signals or the timeout period is exceeded. The ``SignalResource``
        operation is useful in cases where you want to send signals from
        anywhere other than an Amazon EC2 instance.

        :param stack_name: The stack name or unique stack ID that includes the resource that you
        want to signal.
        :param logical_resource_id: The logical ID of the resource that you want to signal.
        :param unique_id: A unique ID of the signal.
        :param status: The status of the signal, which is either success or failure.
        """
        raise NotImplementedError

    @handler("StopStackSetOperation")
    def stop_stack_set_operation(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        operation_id: ClientRequestToken,
        call_as: CallAs = None,
    ) -> StopStackSetOperationOutput:
        """Stops an in-progress operation on a stack set and its associated stack
        instances. StackSets will cancel all the unstarted stack instance
        deployments and wait for those are in-progress to complete.

        :param stack_set_name: The name or unique ID of the stack set that you want to stop the
        operation for.
        :param operation_id: The ID of the stack operation.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: StopStackSetOperationOutput
        :raises StackSetNotFoundException:
        :raises OperationNotFoundException:
        :raises InvalidOperationException:
        """
        raise NotImplementedError

    @handler("TestType", expand=False)
    def test_type(
        self, context: RequestContext, request: TestTypeInput
    ) -> TestTypeOutput:
        """Tests a registered extension to make sure it meets all necessary
        requirements for being published in the CloudFormation registry.

        -  For resource types, this includes passing all contracts tests defined
           for the type.

        -  For modules, this includes determining if the module's model meets
           all necessary requirements.

        For more information, see `Testing your public extension prior to
        publishing <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing>`__
        in the *CloudFormation CLI User Guide*.

        If you don't specify a version, CloudFormation uses the default version
        of the extension in your account and region for testing.

        To perform testing, CloudFormation assumes the execution role specified
        when the type was registered. For more information, see
        `RegisterType <AWSCloudFormation/latest/APIReference/API_RegisterType.html>`__.

        Once you've initiated testing on an extension using ``TestType``, you
        can use
        `DescribeType <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html>`__
        to monitor the current test status and test status description for the
        extension.

        An extension must have a test status of ``PASSED`` before it can be
        published. For more information, see `Publishing extensions to make them
        available for public
        use <https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html>`__
        in the *CloudFormation CLI User Guide*.

        :param arn: The Amazon Resource Name (ARN) of the extension.
        :param type: The type of the extension to test.
        :param type_name: The name of the extension to test.
        :param version_id: The version of the extension to test.
        :param log_delivery_bucket: The S3 bucket to which CloudFormation delivers the contract test
        execution logs.
        :returns: TestTypeOutput
        :raises CFNRegistryException:
        :raises TypeNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateStack")
    def update_stack(
        self,
        context: RequestContext,
        stack_name: StackName,
        template_body: TemplateBody = None,
        template_url: TemplateURL = None,
        use_previous_template: UsePreviousTemplate = None,
        stack_policy_during_update_body: StackPolicyDuringUpdateBody = None,
        stack_policy_during_update_url: StackPolicyDuringUpdateURL = None,
        parameters: Parameters = None,
        capabilities: Capabilities = None,
        resource_types: ResourceTypes = None,
        role_arn: RoleARN = None,
        rollback_configuration: RollbackConfiguration = None,
        stack_policy_body: StackPolicyBody = None,
        stack_policy_url: StackPolicyURL = None,
        notification_arns: NotificationARNs = None,
        tags: Tags = None,
        disable_rollback: DisableRollback = None,
        client_request_token: ClientRequestToken = None,
    ) -> UpdateStackOutput:
        """Updates a stack as specified in the template. After the call completes
        successfully, the stack update starts. You can check the status of the
        stack through the DescribeStacks action.

        To get a copy of the template for an existing stack, you can use the
        GetTemplate action.

        For more information about creating an update template, updating a
        stack, and monitoring the progress of the update, see `Updating a
        Stack <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html>`__.

        :param stack_name: The name or unique stack ID of the stack to update.
        :param template_body: Structure containing the template body with a minimum length of 1 byte
        and a maximum length of 51,200 bytes.
        :param template_url: Location of file containing the template body.
        :param use_previous_template: Reuse the existing template that is associated with the stack that you
        are updating.
        :param stack_policy_during_update_body: Structure containing the temporary overriding stack policy body.
        :param stack_policy_during_update_url: Location of a file containing the temporary overriding stack policy.
        :param parameters: A list of ``Parameter`` structures that specify input parameters for the
        stack.
        :param capabilities: In some cases, you must explicitly acknowledge that your stack template
        contains certain capabilities in order for CloudFormation to update the
        stack.
        :param resource_types: The template resource types that you have permissions to work with for
        this update stack action, such as ``AWS::EC2::Instance``,
        ``AWS::EC2::*``, or ``Custom::MyCustomInstance``.
        :param role_arn: The Amazon Resource Name (ARN) of an Identity and Access Management
        (IAM) role that CloudFormation assumes to update the stack.
        :param rollback_configuration: The rollback triggers for CloudFormation to monitor during stack
        creation and updating operations, and for the specified monitoring
        period afterwards.
        :param stack_policy_body: Structure containing a new stack policy body.
        :param stack_policy_url: Location of a file containing the updated stack policy.
        :param notification_arns: Amazon Simple Notification Service topic Amazon Resource Names (ARNs)
        that CloudFormation associates with the stack.
        :param tags: Key-value pairs to associate with this stack.
        :param disable_rollback: Preserve the state of previously provisioned resources when an operation
        fails.
        :param client_request_token: A unique identifier for this ``UpdateStack`` request.
        :returns: UpdateStackOutput
        :raises InsufficientCapabilitiesException:
        :raises TokenAlreadyExistsException:
        """
        raise NotImplementedError

    @handler("UpdateStackInstances")
    def update_stack_instances(
        self,
        context: RequestContext,
        stack_set_name: StackSetNameOrId,
        regions: RegionList,
        accounts: AccountList = None,
        deployment_targets: DeploymentTargets = None,
        parameter_overrides: Parameters = None,
        operation_preferences: StackSetOperationPreferences = None,
        operation_id: ClientRequestToken = None,
        call_as: CallAs = None,
    ) -> UpdateStackInstancesOutput:
        """Updates the parameter values for stack instances for the specified
        accounts, within the specified Amazon Web Services Regions. A stack
        instance refers to a stack in a specific account and Region.

        You can only update stack instances in Amazon Web Services Regions and
        accounts where they already exist; to create additional stack instances,
        use
        `CreateStackInstances <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html>`__.

        During stack set updates, any parameters overridden for a stack instance
        aren't updated, but retain their overridden value.

        You can only update the parameter *values* that are specified in the
        stack set; to add or delete a parameter itself, use
        `UpdateStackSet <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html>`__
        to update the stack set template. If you add a parameter to a template,
        before you can override the parameter value specified in the stack set
        you must first use
        `UpdateStackSet <https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html>`__
        to update all stack instances with the updated template and parameter
        value specified in the stack set. Once a stack instance has been updated
        with the new parameter, you can then override the parameter value using
        ``UpdateStackInstances``.

        :param stack_set_name: The name or unique ID of the stack set associated with the stack
        instances.
        :param regions: The names of one or more Amazon Web Services Regions in which you want
        to update parameter values for stack instances.
        :param accounts: [Self-managed permissions] The names of one or more Amazon Web Services
        accounts for which you want to update parameter values for stack
        instances.
        :param deployment_targets: [Service-managed permissions] The Organizations accounts for which you
        want to update parameter values for stack instances.
        :param parameter_overrides: A list of input parameters whose values you want to update for the
        specified stack instances.
        :param operation_preferences: Preferences for how CloudFormation performs this stack set operation.
        :param operation_id: The unique identifier for this stack set operation.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :returns: UpdateStackInstancesOutput
        :raises StackSetNotFoundException:
        :raises StackInstanceNotFoundException:
        :raises OperationInProgressException:
        :raises OperationIdAlreadyExistsException:
        :raises StaleRequestException:
        :raises InvalidOperationException:
        """
        raise NotImplementedError

    @handler("UpdateStackSet")
    def update_stack_set(
        self,
        context: RequestContext,
        stack_set_name: StackSetName,
        description: Description = None,
        template_body: TemplateBody = None,
        template_url: TemplateURL = None,
        use_previous_template: UsePreviousTemplate = None,
        parameters: Parameters = None,
        capabilities: Capabilities = None,
        tags: Tags = None,
        operation_preferences: StackSetOperationPreferences = None,
        administration_role_arn: RoleARN = None,
        execution_role_name: ExecutionRoleName = None,
        deployment_targets: DeploymentTargets = None,
        permission_model: PermissionModels = None,
        auto_deployment: AutoDeployment = None,
        operation_id: ClientRequestToken = None,
        accounts: AccountList = None,
        regions: RegionList = None,
        call_as: CallAs = None,
        managed_execution: ManagedExecution = None,
    ) -> UpdateStackSetOutput:
        """Updates the stack set, and associated stack instances in the specified
        accounts and Amazon Web Services Regions.

        Even if the stack set operation created by updating the stack set fails
        (completely or partially, below or above a specified failure tolerance),
        the stack set is updated with your changes. Subsequent
        CreateStackInstances calls on the specified stack set use the updated
        stack set.

        :param stack_set_name: The name or unique ID of the stack set that you want to update.
        :param description: A brief description of updates that you are making.
        :param template_body: The structure that contains the template body, with a minimum length of
        1 byte and a maximum length of 51,200 bytes.
        :param template_url: The location of the file that contains the template body.
        :param use_previous_template: Use the existing template that's associated with the stack set that
        you're updating.
        :param parameters: A list of input parameters for the stack set template.
        :param capabilities: In some cases, you must explicitly acknowledge that your stack template
        contains certain capabilities in order for CloudFormation to update the
        stack set and its associated stack instances.
        :param tags: The key-value pairs to associate with this stack set and the stacks
        created from it.
        :param operation_preferences: Preferences for how CloudFormation performs this stack set operation.
        :param administration_role_arn: The Amazon Resource Number (ARN) of the IAM role to use to update this
        stack set.
        :param execution_role_name: The name of the IAM execution role to use to update the stack set.
        :param deployment_targets: [Service-managed permissions] The Organizations accounts in which to
        update associated stack instances.
        :param permission_model: Describes how the IAM roles required for stack set operations are
        created.
        :param auto_deployment: [Service-managed permissions] Describes whether StackSets automatically
        deploys to Organizations accounts that are added to a target
        organization or organizational unit (OU).
        :param operation_id: The unique ID for this stack set operation.
        :param accounts: [Self-managed permissions] The accounts in which to update associated
        stack instances.
        :param regions: The Amazon Web Services Regions in which to update associated stack
        instances.
        :param call_as: [Service-managed permissions] Specifies whether you are acting as an
        account administrator in the organization's management account or as a
        delegated administrator in a member account.
        :param managed_execution: Describes whether StackSets performs non-conflicting operations
        concurrently and queues conflicting operations.
        :returns: UpdateStackSetOutput
        :raises StackSetNotFoundException:
        :raises OperationInProgressException:
        :raises OperationIdAlreadyExistsException:
        :raises StaleRequestException:
        :raises InvalidOperationException:
        :raises StackInstanceNotFoundException:
        """
        raise NotImplementedError

    @handler("UpdateTerminationProtection")
    def update_termination_protection(
        self,
        context: RequestContext,
        enable_termination_protection: EnableTerminationProtection,
        stack_name: StackNameOrId,
    ) -> UpdateTerminationProtectionOutput:
        """Updates termination protection for the specified stack. If a user
        attempts to delete a stack with termination protection enabled, the
        operation fails and the stack remains unchanged. For more information,
        see `Protecting a Stack From Being
        Deleted <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html>`__
        in the *CloudFormation User Guide*.

        For `nested
        stacks <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html>`__,
        termination protection is set on the root stack and can't be changed
        directly on the nested stack.

        :param enable_termination_protection: Whether to enable termination protection on the specified stack.
        :param stack_name: The name or unique ID of the stack for which you want to set termination
        protection.
        :returns: UpdateTerminationProtectionOutput
        """
        raise NotImplementedError

    @handler("ValidateTemplate")
    def validate_template(
        self,
        context: RequestContext,
        template_body: TemplateBody = None,
        template_url: TemplateURL = None,
    ) -> ValidateTemplateOutput:
        """Validates a specified template. CloudFormation first checks if the
        template is valid JSON. If it isn't, CloudFormation checks if the
        template is valid YAML. If both these checks fail, CloudFormation
        returns a template validation error.

        :param template_body: Structure containing the template body with a minimum length of 1 byte
        and a maximum length of 51,200 bytes.
        :param template_url: Location of file containing the template body.
        :returns: ValidateTemplateOutput
        """
        raise NotImplementedError
