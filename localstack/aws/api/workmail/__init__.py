import sys
from datetime import datetime
from typing import List, Optional

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

AccessControlRuleAction = str
AccessControlRuleDescription = str
AccessControlRuleName = str
AmazonResourceName = str
Boolean = bool
BooleanObject = bool
Description = str
DeviceId = str
DeviceModel = str
DeviceOperatingSystem = str
DeviceType = str
DeviceUserAgent = str
DirectoryId = str
DomainName = str
EmailAddress = str
EntityIdentifier = str
GroupName = str
HostedZoneId = str
IdempotencyClientToken = str
IpAddress = str
IpRange = str
KmsKeyArn = str
LogGroupArn = str
MailboxExportErrorInfo = str
MailboxExportJobId = str
MailboxQuota = int
MailboxSize = float
MaxResults = int
MobileDeviceAccessRuleDescription = str
MobileDeviceAccessRuleId = str
MobileDeviceAccessRuleName = str
NextToken = str
OrganizationId = str
OrganizationName = str
Password = str
Percentage = int
PolicyDescription = str
ResourceId = str
ResourceName = str
RetentionPeriod = int
RoleArn = str
S3BucketName = str
S3ObjectKey = str
ShortString = str
String = str
TagKey = str
TagValue = str
UserName = str
WorkMailDomainName = str
WorkMailIdentifier = str


class AccessControlRuleEffect(str):
    ALLOW = "ALLOW"
    DENY = "DENY"


class DnsRecordVerificationStatus(str):
    PENDING = "PENDING"
    VERIFIED = "VERIFIED"
    FAILED = "FAILED"


class EntityState(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    DELETED = "DELETED"


class FolderName(str):
    INBOX = "INBOX"
    DELETED_ITEMS = "DELETED_ITEMS"
    SENT_ITEMS = "SENT_ITEMS"
    DRAFTS = "DRAFTS"
    JUNK_EMAIL = "JUNK_EMAIL"


class MailboxExportJobState(str):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class MemberType(str):
    GROUP = "GROUP"
    USER = "USER"


class MobileDeviceAccessRuleEffect(str):
    ALLOW = "ALLOW"
    DENY = "DENY"


class PermissionType(str):
    FULL_ACCESS = "FULL_ACCESS"
    SEND_AS = "SEND_AS"
    SEND_ON_BEHALF = "SEND_ON_BEHALF"


class ResourceType(str):
    ROOM = "ROOM"
    EQUIPMENT = "EQUIPMENT"


class RetentionAction(str):
    NONE = "NONE"
    DELETE = "DELETE"
    PERMANENTLY_DELETE = "PERMANENTLY_DELETE"


class UserRole(str):
    USER = "USER"
    RESOURCE = "RESOURCE"
    SYSTEM_USER = "SYSTEM_USER"


class DirectoryInUseException(ServiceException):
    Message: Optional[String]


class DirectoryServiceAuthenticationFailedException(ServiceException):
    Message: Optional[String]


class DirectoryUnavailableException(ServiceException):
    Message: Optional[String]


class EmailAddressInUseException(ServiceException):
    Message: Optional[String]


class EntityAlreadyRegisteredException(ServiceException):
    Message: Optional[String]


class EntityNotFoundException(ServiceException):
    Message: Optional[String]


class EntityStateException(ServiceException):
    Message: Optional[String]


class InvalidConfigurationException(ServiceException):
    Message: Optional[String]


class InvalidCustomSesConfigurationException(ServiceException):
    Message: Optional[String]


class InvalidParameterException(ServiceException):
    Message: Optional[String]


class InvalidPasswordException(ServiceException):
    Message: Optional[String]


class LimitExceededException(ServiceException):
    Message: Optional[String]


class MailDomainInUseException(ServiceException):
    Message: Optional[String]


class MailDomainNotFoundException(ServiceException):
    Message: Optional[String]


class MailDomainStateException(ServiceException):
    Message: Optional[String]


class NameAvailabilityException(ServiceException):
    Message: Optional[String]


class OrganizationNotFoundException(ServiceException):
    Message: Optional[String]


class OrganizationStateException(ServiceException):
    Message: Optional[String]


class ReservedNameException(ServiceException):
    Message: Optional[String]


class ResourceNotFoundException(ServiceException):
    Message: Optional[String]


class TooManyTagsException(ServiceException):
    Message: Optional[String]


class UnsupportedOperationException(ServiceException):
    Message: Optional[String]


Timestamp = datetime
UserIdList = List[WorkMailIdentifier]
ActionsList = List[AccessControlRuleAction]
IpRangeList = List[IpRange]


class AccessControlRule(TypedDict, total=False):
    Name: Optional[AccessControlRuleName]
    Effect: Optional[AccessControlRuleEffect]
    Description: Optional[AccessControlRuleDescription]
    IpRanges: Optional[IpRangeList]
    NotIpRanges: Optional[IpRangeList]
    Actions: Optional[ActionsList]
    NotActions: Optional[ActionsList]
    UserIds: Optional[UserIdList]
    NotUserIds: Optional[UserIdList]
    DateCreated: Optional[Timestamp]
    DateModified: Optional[Timestamp]


AccessControlRuleNameList = List[AccessControlRuleName]
AccessControlRulesList = List[AccessControlRule]
Aliases = List[EmailAddress]


class AssociateDelegateToResourceRequest(ServiceRequest):
    OrganizationId: OrganizationId
    ResourceId: ResourceId
    EntityId: WorkMailIdentifier


class AssociateDelegateToResourceResponse(TypedDict, total=False):
    pass


class AssociateMemberToGroupRequest(ServiceRequest):
    OrganizationId: OrganizationId
    GroupId: WorkMailIdentifier
    MemberId: WorkMailIdentifier


class AssociateMemberToGroupResponse(TypedDict, total=False):
    pass


class BookingOptions(TypedDict, total=False):
    AutoAcceptRequests: Optional[Boolean]
    AutoDeclineRecurringRequests: Optional[Boolean]
    AutoDeclineConflictingRequests: Optional[Boolean]


class CancelMailboxExportJobRequest(ServiceRequest):
    ClientToken: IdempotencyClientToken
    JobId: MailboxExportJobId
    OrganizationId: OrganizationId


class CancelMailboxExportJobResponse(TypedDict, total=False):
    pass


class CreateAliasRequest(ServiceRequest):
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier
    Alias: EmailAddress


class CreateAliasResponse(TypedDict, total=False):
    pass


class CreateGroupRequest(ServiceRequest):
    OrganizationId: OrganizationId
    Name: GroupName


class CreateGroupResponse(TypedDict, total=False):
    GroupId: Optional[WorkMailIdentifier]


DeviceUserAgentList = List[DeviceUserAgent]
DeviceOperatingSystemList = List[DeviceOperatingSystem]
DeviceModelList = List[DeviceModel]
DeviceTypeList = List[DeviceType]


class CreateMobileDeviceAccessRuleRequest(ServiceRequest):
    OrganizationId: OrganizationId
    ClientToken: Optional[IdempotencyClientToken]
    Name: MobileDeviceAccessRuleName
    Description: Optional[MobileDeviceAccessRuleDescription]
    Effect: MobileDeviceAccessRuleEffect
    DeviceTypes: Optional[DeviceTypeList]
    NotDeviceTypes: Optional[DeviceTypeList]
    DeviceModels: Optional[DeviceModelList]
    NotDeviceModels: Optional[DeviceModelList]
    DeviceOperatingSystems: Optional[DeviceOperatingSystemList]
    NotDeviceOperatingSystems: Optional[DeviceOperatingSystemList]
    DeviceUserAgents: Optional[DeviceUserAgentList]
    NotDeviceUserAgents: Optional[DeviceUserAgentList]


class CreateMobileDeviceAccessRuleResponse(TypedDict, total=False):
    MobileDeviceAccessRuleId: Optional[MobileDeviceAccessRuleId]


class Domain(TypedDict, total=False):
    DomainName: Optional[DomainName]
    HostedZoneId: Optional[HostedZoneId]


Domains = List[Domain]


class CreateOrganizationRequest(ServiceRequest):
    DirectoryId: Optional[DirectoryId]
    Alias: OrganizationName
    ClientToken: Optional[IdempotencyClientToken]
    Domains: Optional[Domains]
    KmsKeyArn: Optional[KmsKeyArn]
    EnableInteroperability: Optional[Boolean]


class CreateOrganizationResponse(TypedDict, total=False):
    OrganizationId: Optional[OrganizationId]


class CreateResourceRequest(ServiceRequest):
    OrganizationId: OrganizationId
    Name: ResourceName
    Type: ResourceType


class CreateResourceResponse(TypedDict, total=False):
    ResourceId: Optional[ResourceId]


class CreateUserRequest(ServiceRequest):
    OrganizationId: OrganizationId
    Name: UserName
    DisplayName: String
    Password: Password


class CreateUserResponse(TypedDict, total=False):
    UserId: Optional[WorkMailIdentifier]


class Delegate(TypedDict, total=False):
    Id: String
    Type: MemberType


class DeleteAccessControlRuleRequest(ServiceRequest):
    OrganizationId: OrganizationId
    Name: AccessControlRuleName


class DeleteAccessControlRuleResponse(TypedDict, total=False):
    pass


class DeleteAliasRequest(ServiceRequest):
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier
    Alias: EmailAddress


class DeleteAliasResponse(TypedDict, total=False):
    pass


class DeleteEmailMonitoringConfigurationRequest(ServiceRequest):
    OrganizationId: OrganizationId


class DeleteEmailMonitoringConfigurationResponse(TypedDict, total=False):
    pass


class DeleteGroupRequest(ServiceRequest):
    OrganizationId: OrganizationId
    GroupId: WorkMailIdentifier


class DeleteGroupResponse(TypedDict, total=False):
    pass


class DeleteMailboxPermissionsRequest(ServiceRequest):
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier
    GranteeId: WorkMailIdentifier


class DeleteMailboxPermissionsResponse(TypedDict, total=False):
    pass


class DeleteMobileDeviceAccessOverrideRequest(ServiceRequest):
    OrganizationId: OrganizationId
    UserId: EntityIdentifier
    DeviceId: DeviceId


class DeleteMobileDeviceAccessOverrideResponse(TypedDict, total=False):
    pass


class DeleteMobileDeviceAccessRuleRequest(ServiceRequest):
    OrganizationId: OrganizationId
    MobileDeviceAccessRuleId: MobileDeviceAccessRuleId


class DeleteMobileDeviceAccessRuleResponse(TypedDict, total=False):
    pass


class DeleteOrganizationRequest(ServiceRequest):
    ClientToken: Optional[IdempotencyClientToken]
    OrganizationId: OrganizationId
    DeleteDirectory: Boolean


class DeleteOrganizationResponse(TypedDict, total=False):
    OrganizationId: Optional[OrganizationId]
    State: Optional[String]


class DeleteResourceRequest(ServiceRequest):
    OrganizationId: OrganizationId
    ResourceId: ResourceId


class DeleteResourceResponse(TypedDict, total=False):
    pass


class DeleteRetentionPolicyRequest(ServiceRequest):
    OrganizationId: OrganizationId
    Id: ShortString


class DeleteRetentionPolicyResponse(TypedDict, total=False):
    pass


class DeleteUserRequest(ServiceRequest):
    OrganizationId: OrganizationId
    UserId: WorkMailIdentifier


class DeleteUserResponse(TypedDict, total=False):
    pass


class DeregisterFromWorkMailRequest(ServiceRequest):
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier


class DeregisterFromWorkMailResponse(TypedDict, total=False):
    pass


class DeregisterMailDomainRequest(ServiceRequest):
    OrganizationId: OrganizationId
    DomainName: WorkMailDomainName


class DeregisterMailDomainResponse(TypedDict, total=False):
    pass


class DescribeEmailMonitoringConfigurationRequest(ServiceRequest):
    OrganizationId: OrganizationId


class DescribeEmailMonitoringConfigurationResponse(TypedDict, total=False):
    RoleArn: Optional[RoleArn]
    LogGroupArn: Optional[LogGroupArn]


class DescribeGroupRequest(ServiceRequest):
    OrganizationId: OrganizationId
    GroupId: WorkMailIdentifier


class DescribeGroupResponse(TypedDict, total=False):
    GroupId: Optional[WorkMailIdentifier]
    Name: Optional[GroupName]
    Email: Optional[EmailAddress]
    State: Optional[EntityState]
    EnabledDate: Optional[Timestamp]
    DisabledDate: Optional[Timestamp]


class DescribeInboundDmarcSettingsRequest(ServiceRequest):
    OrganizationId: OrganizationId


class DescribeInboundDmarcSettingsResponse(TypedDict, total=False):
    Enforced: Optional[Boolean]


class DescribeMailboxExportJobRequest(ServiceRequest):
    JobId: MailboxExportJobId
    OrganizationId: OrganizationId


class DescribeMailboxExportJobResponse(TypedDict, total=False):
    EntityId: Optional[WorkMailIdentifier]
    Description: Optional[Description]
    RoleArn: Optional[RoleArn]
    KmsKeyArn: Optional[KmsKeyArn]
    S3BucketName: Optional[S3BucketName]
    S3Prefix: Optional[S3ObjectKey]
    S3Path: Optional[S3ObjectKey]
    EstimatedProgress: Optional[Percentage]
    State: Optional[MailboxExportJobState]
    ErrorInfo: Optional[MailboxExportErrorInfo]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]


class DescribeOrganizationRequest(ServiceRequest):
    OrganizationId: OrganizationId


class DescribeOrganizationResponse(TypedDict, total=False):
    OrganizationId: Optional[OrganizationId]
    Alias: Optional[OrganizationName]
    State: Optional[String]
    DirectoryId: Optional[String]
    DirectoryType: Optional[String]
    DefaultMailDomain: Optional[String]
    CompletedDate: Optional[Timestamp]
    ErrorMessage: Optional[String]
    ARN: Optional[AmazonResourceName]


class DescribeResourceRequest(ServiceRequest):
    OrganizationId: OrganizationId
    ResourceId: ResourceId


class DescribeResourceResponse(TypedDict, total=False):
    ResourceId: Optional[ResourceId]
    Email: Optional[EmailAddress]
    Name: Optional[ResourceName]
    Type: Optional[ResourceType]
    BookingOptions: Optional[BookingOptions]
    State: Optional[EntityState]
    EnabledDate: Optional[Timestamp]
    DisabledDate: Optional[Timestamp]


class DescribeUserRequest(ServiceRequest):
    OrganizationId: OrganizationId
    UserId: WorkMailIdentifier


class DescribeUserResponse(TypedDict, total=False):
    UserId: Optional[WorkMailIdentifier]
    Name: Optional[UserName]
    Email: Optional[EmailAddress]
    DisplayName: Optional[String]
    State: Optional[EntityState]
    UserRole: Optional[UserRole]
    EnabledDate: Optional[Timestamp]
    DisabledDate: Optional[Timestamp]


class DisassociateDelegateFromResourceRequest(ServiceRequest):
    OrganizationId: OrganizationId
    ResourceId: ResourceId
    EntityId: WorkMailIdentifier


class DisassociateDelegateFromResourceResponse(TypedDict, total=False):
    pass


class DisassociateMemberFromGroupRequest(ServiceRequest):
    OrganizationId: OrganizationId
    GroupId: WorkMailIdentifier
    MemberId: WorkMailIdentifier


class DisassociateMemberFromGroupResponse(TypedDict, total=False):
    pass


class DnsRecord(TypedDict, total=False):
    Type: Optional[String]
    Hostname: Optional[String]
    Value: Optional[String]


DnsRecords = List[DnsRecord]


class FolderConfiguration(TypedDict, total=False):
    Name: FolderName
    Action: RetentionAction
    Period: Optional[RetentionPeriod]


FolderConfigurations = List[FolderConfiguration]


class GetAccessControlEffectRequest(ServiceRequest):
    OrganizationId: OrganizationId
    IpAddress: IpAddress
    Action: AccessControlRuleAction
    UserId: WorkMailIdentifier


class GetAccessControlEffectResponse(TypedDict, total=False):
    Effect: Optional[AccessControlRuleEffect]
    MatchedRules: Optional[AccessControlRuleNameList]


class GetDefaultRetentionPolicyRequest(ServiceRequest):
    OrganizationId: OrganizationId


class GetDefaultRetentionPolicyResponse(TypedDict, total=False):
    Id: Optional[ShortString]
    Name: Optional[ShortString]
    Description: Optional[String]
    FolderConfigurations: Optional[FolderConfigurations]


class GetMailDomainRequest(ServiceRequest):
    OrganizationId: OrganizationId
    DomainName: WorkMailDomainName


class GetMailDomainResponse(TypedDict, total=False):
    Records: Optional[DnsRecords]
    IsTestDomain: Optional[Boolean]
    IsDefault: Optional[Boolean]
    OwnershipVerificationStatus: Optional[DnsRecordVerificationStatus]
    DkimVerificationStatus: Optional[DnsRecordVerificationStatus]


class GetMailboxDetailsRequest(ServiceRequest):
    OrganizationId: OrganizationId
    UserId: WorkMailIdentifier


class GetMailboxDetailsResponse(TypedDict, total=False):
    MailboxQuota: Optional[MailboxQuota]
    MailboxSize: Optional[MailboxSize]


class GetMobileDeviceAccessEffectRequest(ServiceRequest):
    OrganizationId: OrganizationId
    DeviceType: Optional[DeviceType]
    DeviceModel: Optional[DeviceModel]
    DeviceOperatingSystem: Optional[DeviceOperatingSystem]
    DeviceUserAgent: Optional[DeviceUserAgent]


class MobileDeviceAccessMatchedRule(TypedDict, total=False):
    MobileDeviceAccessRuleId: Optional[MobileDeviceAccessRuleId]
    Name: Optional[MobileDeviceAccessRuleName]


MobileDeviceAccessMatchedRuleList = List[MobileDeviceAccessMatchedRule]


class GetMobileDeviceAccessEffectResponse(TypedDict, total=False):
    Effect: Optional[MobileDeviceAccessRuleEffect]
    MatchedRules: Optional[MobileDeviceAccessMatchedRuleList]


class GetMobileDeviceAccessOverrideRequest(ServiceRequest):
    OrganizationId: OrganizationId
    UserId: EntityIdentifier
    DeviceId: DeviceId


class GetMobileDeviceAccessOverrideResponse(TypedDict, total=False):
    UserId: Optional[WorkMailIdentifier]
    DeviceId: Optional[DeviceId]
    Effect: Optional[MobileDeviceAccessRuleEffect]
    Description: Optional[MobileDeviceAccessRuleDescription]
    DateCreated: Optional[Timestamp]
    DateModified: Optional[Timestamp]


class Group(TypedDict, total=False):
    Id: Optional[WorkMailIdentifier]
    Email: Optional[EmailAddress]
    Name: Optional[GroupName]
    State: Optional[EntityState]
    EnabledDate: Optional[Timestamp]
    DisabledDate: Optional[Timestamp]


Groups = List[Group]


class MailboxExportJob(TypedDict, total=False):
    JobId: Optional[MailboxExportJobId]
    EntityId: Optional[WorkMailIdentifier]
    Description: Optional[Description]
    S3BucketName: Optional[S3BucketName]
    S3Path: Optional[S3ObjectKey]
    EstimatedProgress: Optional[Percentage]
    State: Optional[MailboxExportJobState]
    StartTime: Optional[Timestamp]
    EndTime: Optional[Timestamp]


Jobs = List[MailboxExportJob]


class ListAccessControlRulesRequest(ServiceRequest):
    OrganizationId: OrganizationId


class ListAccessControlRulesResponse(TypedDict, total=False):
    Rules: Optional[AccessControlRulesList]


class ListAliasesRequest(ServiceRequest):
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListAliasesResponse(TypedDict, total=False):
    Aliases: Optional[Aliases]
    NextToken: Optional[NextToken]


class ListGroupMembersRequest(ServiceRequest):
    OrganizationId: OrganizationId
    GroupId: WorkMailIdentifier
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class Member(TypedDict, total=False):
    Id: Optional[String]
    Name: Optional[String]
    Type: Optional[MemberType]
    State: Optional[EntityState]
    EnabledDate: Optional[Timestamp]
    DisabledDate: Optional[Timestamp]


Members = List[Member]


class ListGroupMembersResponse(TypedDict, total=False):
    Members: Optional[Members]
    NextToken: Optional[NextToken]


class ListGroupsRequest(ServiceRequest):
    OrganizationId: OrganizationId
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListGroupsResponse(TypedDict, total=False):
    Groups: Optional[Groups]
    NextToken: Optional[NextToken]


class ListMailDomainsRequest(ServiceRequest):
    OrganizationId: OrganizationId
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class MailDomainSummary(TypedDict, total=False):
    DomainName: Optional[DomainName]
    DefaultDomain: Optional[Boolean]


MailDomains = List[MailDomainSummary]


class ListMailDomainsResponse(TypedDict, total=False):
    MailDomains: Optional[MailDomains]
    NextToken: Optional[NextToken]


class ListMailboxExportJobsRequest(ServiceRequest):
    OrganizationId: OrganizationId
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class ListMailboxExportJobsResponse(TypedDict, total=False):
    Jobs: Optional[Jobs]
    NextToken: Optional[NextToken]


class ListMailboxPermissionsRequest(ServiceRequest):
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


PermissionValues = List[PermissionType]


class Permission(TypedDict, total=False):
    GranteeId: WorkMailIdentifier
    GranteeType: MemberType
    PermissionValues: PermissionValues


Permissions = List[Permission]


class ListMailboxPermissionsResponse(TypedDict, total=False):
    Permissions: Optional[Permissions]
    NextToken: Optional[NextToken]


class ListMobileDeviceAccessOverridesRequest(ServiceRequest):
    OrganizationId: OrganizationId
    UserId: Optional[EntityIdentifier]
    DeviceId: Optional[DeviceId]
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class MobileDeviceAccessOverride(TypedDict, total=False):
    UserId: Optional[WorkMailIdentifier]
    DeviceId: Optional[DeviceId]
    Effect: Optional[MobileDeviceAccessRuleEffect]
    Description: Optional[MobileDeviceAccessRuleDescription]
    DateCreated: Optional[Timestamp]
    DateModified: Optional[Timestamp]


MobileDeviceAccessOverridesList = List[MobileDeviceAccessOverride]


class ListMobileDeviceAccessOverridesResponse(TypedDict, total=False):
    Overrides: Optional[MobileDeviceAccessOverridesList]
    NextToken: Optional[NextToken]


class ListMobileDeviceAccessRulesRequest(ServiceRequest):
    OrganizationId: OrganizationId


class MobileDeviceAccessRule(TypedDict, total=False):
    MobileDeviceAccessRuleId: Optional[MobileDeviceAccessRuleId]
    Name: Optional[MobileDeviceAccessRuleName]
    Description: Optional[MobileDeviceAccessRuleDescription]
    Effect: Optional[MobileDeviceAccessRuleEffect]
    DeviceTypes: Optional[DeviceTypeList]
    NotDeviceTypes: Optional[DeviceTypeList]
    DeviceModels: Optional[DeviceModelList]
    NotDeviceModels: Optional[DeviceModelList]
    DeviceOperatingSystems: Optional[DeviceOperatingSystemList]
    NotDeviceOperatingSystems: Optional[DeviceOperatingSystemList]
    DeviceUserAgents: Optional[DeviceUserAgentList]
    NotDeviceUserAgents: Optional[DeviceUserAgentList]
    DateCreated: Optional[Timestamp]
    DateModified: Optional[Timestamp]


MobileDeviceAccessRulesList = List[MobileDeviceAccessRule]


class ListMobileDeviceAccessRulesResponse(TypedDict, total=False):
    Rules: Optional[MobileDeviceAccessRulesList]


class ListOrganizationsRequest(ServiceRequest):
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class OrganizationSummary(TypedDict, total=False):
    OrganizationId: Optional[OrganizationId]
    Alias: Optional[OrganizationName]
    DefaultMailDomain: Optional[DomainName]
    ErrorMessage: Optional[String]
    State: Optional[String]


OrganizationSummaries = List[OrganizationSummary]


class ListOrganizationsResponse(TypedDict, total=False):
    OrganizationSummaries: Optional[OrganizationSummaries]
    NextToken: Optional[NextToken]


class ListResourceDelegatesRequest(ServiceRequest):
    OrganizationId: OrganizationId
    ResourceId: WorkMailIdentifier
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


ResourceDelegates = List[Delegate]


class ListResourceDelegatesResponse(TypedDict, total=False):
    Delegates: Optional[ResourceDelegates]
    NextToken: Optional[NextToken]


class ListResourcesRequest(ServiceRequest):
    OrganizationId: OrganizationId
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class Resource(TypedDict, total=False):
    Id: Optional[WorkMailIdentifier]
    Email: Optional[EmailAddress]
    Name: Optional[ResourceName]
    Type: Optional[ResourceType]
    State: Optional[EntityState]
    EnabledDate: Optional[Timestamp]
    DisabledDate: Optional[Timestamp]


Resources = List[Resource]


class ListResourcesResponse(TypedDict, total=False):
    Resources: Optional[Resources]
    NextToken: Optional[NextToken]


class ListTagsForResourceRequest(ServiceRequest):
    ResourceARN: AmazonResourceName


class Tag(TypedDict, total=False):
    Key: TagKey
    Value: TagValue


TagList = List[Tag]


class ListTagsForResourceResponse(TypedDict, total=False):
    Tags: Optional[TagList]


class ListUsersRequest(ServiceRequest):
    OrganizationId: OrganizationId
    NextToken: Optional[NextToken]
    MaxResults: Optional[MaxResults]


class User(TypedDict, total=False):
    Id: Optional[WorkMailIdentifier]
    Email: Optional[EmailAddress]
    Name: Optional[UserName]
    DisplayName: Optional[String]
    State: Optional[EntityState]
    UserRole: Optional[UserRole]
    EnabledDate: Optional[Timestamp]
    DisabledDate: Optional[Timestamp]


Users = List[User]


class ListUsersResponse(TypedDict, total=False):
    Users: Optional[Users]
    NextToken: Optional[NextToken]


class PutAccessControlRuleRequest(ServiceRequest):
    Name: AccessControlRuleName
    Effect: AccessControlRuleEffect
    Description: AccessControlRuleDescription
    IpRanges: Optional[IpRangeList]
    NotIpRanges: Optional[IpRangeList]
    Actions: Optional[ActionsList]
    NotActions: Optional[ActionsList]
    UserIds: Optional[UserIdList]
    NotUserIds: Optional[UserIdList]
    OrganizationId: OrganizationId


class PutAccessControlRuleResponse(TypedDict, total=False):
    pass


class PutEmailMonitoringConfigurationRequest(ServiceRequest):
    OrganizationId: OrganizationId
    RoleArn: RoleArn
    LogGroupArn: LogGroupArn


class PutEmailMonitoringConfigurationResponse(TypedDict, total=False):
    pass


class PutInboundDmarcSettingsRequest(ServiceRequest):
    OrganizationId: OrganizationId
    Enforced: BooleanObject


class PutInboundDmarcSettingsResponse(TypedDict, total=False):
    pass


class PutMailboxPermissionsRequest(ServiceRequest):
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier
    GranteeId: WorkMailIdentifier
    PermissionValues: PermissionValues


class PutMailboxPermissionsResponse(TypedDict, total=False):
    pass


class PutMobileDeviceAccessOverrideRequest(ServiceRequest):
    OrganizationId: OrganizationId
    UserId: EntityIdentifier
    DeviceId: DeviceId
    Effect: MobileDeviceAccessRuleEffect
    Description: Optional[MobileDeviceAccessRuleDescription]


class PutMobileDeviceAccessOverrideResponse(TypedDict, total=False):
    pass


class PutRetentionPolicyRequest(ServiceRequest):
    OrganizationId: OrganizationId
    Id: Optional[ShortString]
    Name: ShortString
    Description: Optional[PolicyDescription]
    FolderConfigurations: FolderConfigurations


class PutRetentionPolicyResponse(TypedDict, total=False):
    pass


class RegisterMailDomainRequest(ServiceRequest):
    ClientToken: Optional[IdempotencyClientToken]
    OrganizationId: OrganizationId
    DomainName: WorkMailDomainName


class RegisterMailDomainResponse(TypedDict, total=False):
    pass


class RegisterToWorkMailRequest(ServiceRequest):
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier
    Email: EmailAddress


class RegisterToWorkMailResponse(TypedDict, total=False):
    pass


class ResetPasswordRequest(ServiceRequest):
    OrganizationId: OrganizationId
    UserId: WorkMailIdentifier
    Password: Password


class ResetPasswordResponse(TypedDict, total=False):
    pass


class StartMailboxExportJobRequest(ServiceRequest):
    ClientToken: IdempotencyClientToken
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier
    Description: Optional[Description]
    RoleArn: RoleArn
    KmsKeyArn: KmsKeyArn
    S3BucketName: S3BucketName
    S3Prefix: S3ObjectKey


class StartMailboxExportJobResponse(TypedDict, total=False):
    JobId: Optional[MailboxExportJobId]


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    ResourceARN: AmazonResourceName
    Tags: TagList


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    ResourceARN: AmazonResourceName
    TagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdateDefaultMailDomainRequest(ServiceRequest):
    OrganizationId: OrganizationId
    DomainName: WorkMailDomainName


class UpdateDefaultMailDomainResponse(TypedDict, total=False):
    pass


class UpdateMailboxQuotaRequest(ServiceRequest):
    OrganizationId: OrganizationId
    UserId: WorkMailIdentifier
    MailboxQuota: MailboxQuota


class UpdateMailboxQuotaResponse(TypedDict, total=False):
    pass


class UpdateMobileDeviceAccessRuleRequest(ServiceRequest):
    OrganizationId: OrganizationId
    MobileDeviceAccessRuleId: MobileDeviceAccessRuleId
    Name: MobileDeviceAccessRuleName
    Description: Optional[MobileDeviceAccessRuleDescription]
    Effect: MobileDeviceAccessRuleEffect
    DeviceTypes: Optional[DeviceTypeList]
    NotDeviceTypes: Optional[DeviceTypeList]
    DeviceModels: Optional[DeviceModelList]
    NotDeviceModels: Optional[DeviceModelList]
    DeviceOperatingSystems: Optional[DeviceOperatingSystemList]
    NotDeviceOperatingSystems: Optional[DeviceOperatingSystemList]
    DeviceUserAgents: Optional[DeviceUserAgentList]
    NotDeviceUserAgents: Optional[DeviceUserAgentList]


class UpdateMobileDeviceAccessRuleResponse(TypedDict, total=False):
    pass


class UpdatePrimaryEmailAddressRequest(ServiceRequest):
    OrganizationId: OrganizationId
    EntityId: WorkMailIdentifier
    Email: EmailAddress


class UpdatePrimaryEmailAddressResponse(TypedDict, total=False):
    pass


class UpdateResourceRequest(ServiceRequest):
    OrganizationId: OrganizationId
    ResourceId: ResourceId
    Name: Optional[ResourceName]
    BookingOptions: Optional[BookingOptions]


class UpdateResourceResponse(TypedDict, total=False):
    pass


class WorkmailApi:

    service = "workmail"
    version = "2017-10-01"

    @handler("AssociateDelegateToResource")
    def associate_delegate_to_resource(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        resource_id: ResourceId,
        entity_id: WorkMailIdentifier,
    ) -> AssociateDelegateToResourceResponse:
        raise NotImplementedError

    @handler("AssociateMemberToGroup")
    def associate_member_to_group(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        group_id: WorkMailIdentifier,
        member_id: WorkMailIdentifier,
    ) -> AssociateMemberToGroupResponse:
        raise NotImplementedError

    @handler("CancelMailboxExportJob")
    def cancel_mailbox_export_job(
        self,
        context: RequestContext,
        client_token: IdempotencyClientToken,
        job_id: MailboxExportJobId,
        organization_id: OrganizationId,
    ) -> CancelMailboxExportJobResponse:
        raise NotImplementedError

    @handler("CreateAlias")
    def create_alias(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
        alias: EmailAddress,
    ) -> CreateAliasResponse:
        raise NotImplementedError

    @handler("CreateGroup")
    def create_group(
        self, context: RequestContext, organization_id: OrganizationId, name: GroupName
    ) -> CreateGroupResponse:
        raise NotImplementedError

    @handler("CreateMobileDeviceAccessRule")
    def create_mobile_device_access_rule(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        name: MobileDeviceAccessRuleName,
        effect: MobileDeviceAccessRuleEffect,
        client_token: IdempotencyClientToken = None,
        description: MobileDeviceAccessRuleDescription = None,
        device_types: DeviceTypeList = None,
        not_device_types: DeviceTypeList = None,
        device_models: DeviceModelList = None,
        not_device_models: DeviceModelList = None,
        device_operating_systems: DeviceOperatingSystemList = None,
        not_device_operating_systems: DeviceOperatingSystemList = None,
        device_user_agents: DeviceUserAgentList = None,
        not_device_user_agents: DeviceUserAgentList = None,
    ) -> CreateMobileDeviceAccessRuleResponse:
        raise NotImplementedError

    @handler("CreateOrganization")
    def create_organization(
        self,
        context: RequestContext,
        alias: OrganizationName,
        directory_id: DirectoryId = None,
        client_token: IdempotencyClientToken = None,
        domains: Domains = None,
        kms_key_arn: KmsKeyArn = None,
        enable_interoperability: Boolean = None,
    ) -> CreateOrganizationResponse:
        raise NotImplementedError

    @handler("CreateResource", expand=False)
    def create_resource(
        self, context: RequestContext, request: CreateResourceRequest
    ) -> CreateResourceResponse:
        raise NotImplementedError

    @handler("CreateUser")
    def create_user(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        name: UserName,
        display_name: String,
        password: Password,
    ) -> CreateUserResponse:
        raise NotImplementedError

    @handler("DeleteAccessControlRule")
    def delete_access_control_rule(
        self, context: RequestContext, organization_id: OrganizationId, name: AccessControlRuleName
    ) -> DeleteAccessControlRuleResponse:
        raise NotImplementedError

    @handler("DeleteAlias")
    def delete_alias(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
        alias: EmailAddress,
    ) -> DeleteAliasResponse:
        raise NotImplementedError

    @handler("DeleteEmailMonitoringConfiguration")
    def delete_email_monitoring_configuration(
        self, context: RequestContext, organization_id: OrganizationId
    ) -> DeleteEmailMonitoringConfigurationResponse:
        raise NotImplementedError

    @handler("DeleteGroup")
    def delete_group(
        self, context: RequestContext, organization_id: OrganizationId, group_id: WorkMailIdentifier
    ) -> DeleteGroupResponse:
        raise NotImplementedError

    @handler("DeleteMailboxPermissions")
    def delete_mailbox_permissions(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
        grantee_id: WorkMailIdentifier,
    ) -> DeleteMailboxPermissionsResponse:
        raise NotImplementedError

    @handler("DeleteMobileDeviceAccessOverride")
    def delete_mobile_device_access_override(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        user_id: EntityIdentifier,
        device_id: DeviceId,
    ) -> DeleteMobileDeviceAccessOverrideResponse:
        raise NotImplementedError

    @handler("DeleteMobileDeviceAccessRule")
    def delete_mobile_device_access_rule(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        mobile_device_access_rule_id: MobileDeviceAccessRuleId,
    ) -> DeleteMobileDeviceAccessRuleResponse:
        raise NotImplementedError

    @handler("DeleteOrganization")
    def delete_organization(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        delete_directory: Boolean,
        client_token: IdempotencyClientToken = None,
    ) -> DeleteOrganizationResponse:
        raise NotImplementedError

    @handler("DeleteResource")
    def delete_resource(
        self, context: RequestContext, organization_id: OrganizationId, resource_id: ResourceId
    ) -> DeleteResourceResponse:
        raise NotImplementedError

    @handler("DeleteRetentionPolicy")
    def delete_retention_policy(
        self, context: RequestContext, organization_id: OrganizationId, id: ShortString
    ) -> DeleteRetentionPolicyResponse:
        raise NotImplementedError

    @handler("DeleteUser")
    def delete_user(
        self, context: RequestContext, organization_id: OrganizationId, user_id: WorkMailIdentifier
    ) -> DeleteUserResponse:
        raise NotImplementedError

    @handler("DeregisterFromWorkMail")
    def deregister_from_work_mail(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
    ) -> DeregisterFromWorkMailResponse:
        raise NotImplementedError

    @handler("DeregisterMailDomain")
    def deregister_mail_domain(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        domain_name: WorkMailDomainName,
    ) -> DeregisterMailDomainResponse:
        raise NotImplementedError

    @handler("DescribeEmailMonitoringConfiguration")
    def describe_email_monitoring_configuration(
        self, context: RequestContext, organization_id: OrganizationId
    ) -> DescribeEmailMonitoringConfigurationResponse:
        raise NotImplementedError

    @handler("DescribeGroup")
    def describe_group(
        self, context: RequestContext, organization_id: OrganizationId, group_id: WorkMailIdentifier
    ) -> DescribeGroupResponse:
        raise NotImplementedError

    @handler("DescribeInboundDmarcSettings")
    def describe_inbound_dmarc_settings(
        self, context: RequestContext, organization_id: OrganizationId
    ) -> DescribeInboundDmarcSettingsResponse:
        raise NotImplementedError

    @handler("DescribeMailboxExportJob")
    def describe_mailbox_export_job(
        self, context: RequestContext, job_id: MailboxExportJobId, organization_id: OrganizationId
    ) -> DescribeMailboxExportJobResponse:
        raise NotImplementedError

    @handler("DescribeOrganization")
    def describe_organization(
        self, context: RequestContext, organization_id: OrganizationId
    ) -> DescribeOrganizationResponse:
        raise NotImplementedError

    @handler("DescribeResource")
    def describe_resource(
        self, context: RequestContext, organization_id: OrganizationId, resource_id: ResourceId
    ) -> DescribeResourceResponse:
        raise NotImplementedError

    @handler("DescribeUser")
    def describe_user(
        self, context: RequestContext, organization_id: OrganizationId, user_id: WorkMailIdentifier
    ) -> DescribeUserResponse:
        raise NotImplementedError

    @handler("DisassociateDelegateFromResource")
    def disassociate_delegate_from_resource(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        resource_id: ResourceId,
        entity_id: WorkMailIdentifier,
    ) -> DisassociateDelegateFromResourceResponse:
        raise NotImplementedError

    @handler("DisassociateMemberFromGroup")
    def disassociate_member_from_group(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        group_id: WorkMailIdentifier,
        member_id: WorkMailIdentifier,
    ) -> DisassociateMemberFromGroupResponse:
        raise NotImplementedError

    @handler("GetAccessControlEffect")
    def get_access_control_effect(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        ip_address: IpAddress,
        action: AccessControlRuleAction,
        user_id: WorkMailIdentifier,
    ) -> GetAccessControlEffectResponse:
        raise NotImplementedError

    @handler("GetDefaultRetentionPolicy")
    def get_default_retention_policy(
        self, context: RequestContext, organization_id: OrganizationId
    ) -> GetDefaultRetentionPolicyResponse:
        raise NotImplementedError

    @handler("GetMailDomain")
    def get_mail_domain(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        domain_name: WorkMailDomainName,
    ) -> GetMailDomainResponse:
        raise NotImplementedError

    @handler("GetMailboxDetails")
    def get_mailbox_details(
        self, context: RequestContext, organization_id: OrganizationId, user_id: WorkMailIdentifier
    ) -> GetMailboxDetailsResponse:
        raise NotImplementedError

    @handler("GetMobileDeviceAccessEffect")
    def get_mobile_device_access_effect(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        device_type: DeviceType = None,
        device_model: DeviceModel = None,
        device_operating_system: DeviceOperatingSystem = None,
        device_user_agent: DeviceUserAgent = None,
    ) -> GetMobileDeviceAccessEffectResponse:
        raise NotImplementedError

    @handler("GetMobileDeviceAccessOverride")
    def get_mobile_device_access_override(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        user_id: EntityIdentifier,
        device_id: DeviceId,
    ) -> GetMobileDeviceAccessOverrideResponse:
        raise NotImplementedError

    @handler("ListAccessControlRules")
    def list_access_control_rules(
        self, context: RequestContext, organization_id: OrganizationId
    ) -> ListAccessControlRulesResponse:
        raise NotImplementedError

    @handler("ListAliases")
    def list_aliases(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
        next_token: NextToken = None,
        max_results: MaxResults = None,
    ) -> ListAliasesResponse:
        raise NotImplementedError

    @handler("ListGroupMembers")
    def list_group_members(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        group_id: WorkMailIdentifier,
        next_token: NextToken = None,
        max_results: MaxResults = None,
    ) -> ListGroupMembersResponse:
        raise NotImplementedError

    @handler("ListGroups")
    def list_groups(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        next_token: NextToken = None,
        max_results: MaxResults = None,
    ) -> ListGroupsResponse:
        raise NotImplementedError

    @handler("ListMailDomains")
    def list_mail_domains(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        max_results: MaxResults = None,
        next_token: NextToken = None,
    ) -> ListMailDomainsResponse:
        raise NotImplementedError

    @handler("ListMailboxExportJobs")
    def list_mailbox_export_jobs(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        next_token: NextToken = None,
        max_results: MaxResults = None,
    ) -> ListMailboxExportJobsResponse:
        raise NotImplementedError

    @handler("ListMailboxPermissions")
    def list_mailbox_permissions(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
        next_token: NextToken = None,
        max_results: MaxResults = None,
    ) -> ListMailboxPermissionsResponse:
        raise NotImplementedError

    @handler("ListMobileDeviceAccessOverrides")
    def list_mobile_device_access_overrides(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        user_id: EntityIdentifier = None,
        device_id: DeviceId = None,
        next_token: NextToken = None,
        max_results: MaxResults = None,
    ) -> ListMobileDeviceAccessOverridesResponse:
        raise NotImplementedError

    @handler("ListMobileDeviceAccessRules")
    def list_mobile_device_access_rules(
        self, context: RequestContext, organization_id: OrganizationId
    ) -> ListMobileDeviceAccessRulesResponse:
        raise NotImplementedError

    @handler("ListOrganizations")
    def list_organizations(
        self, context: RequestContext, next_token: NextToken = None, max_results: MaxResults = None
    ) -> ListOrganizationsResponse:
        raise NotImplementedError

    @handler("ListResourceDelegates")
    def list_resource_delegates(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        resource_id: WorkMailIdentifier,
        next_token: NextToken = None,
        max_results: MaxResults = None,
    ) -> ListResourceDelegatesResponse:
        raise NotImplementedError

    @handler("ListResources")
    def list_resources(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        next_token: NextToken = None,
        max_results: MaxResults = None,
    ) -> ListResourcesResponse:
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: AmazonResourceName
    ) -> ListTagsForResourceResponse:
        raise NotImplementedError

    @handler("ListUsers")
    def list_users(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        next_token: NextToken = None,
        max_results: MaxResults = None,
    ) -> ListUsersResponse:
        raise NotImplementedError

    @handler("PutAccessControlRule")
    def put_access_control_rule(
        self,
        context: RequestContext,
        name: AccessControlRuleName,
        effect: AccessControlRuleEffect,
        description: AccessControlRuleDescription,
        organization_id: OrganizationId,
        ip_ranges: IpRangeList = None,
        not_ip_ranges: IpRangeList = None,
        actions: ActionsList = None,
        not_actions: ActionsList = None,
        user_ids: UserIdList = None,
        not_user_ids: UserIdList = None,
    ) -> PutAccessControlRuleResponse:
        raise NotImplementedError

    @handler("PutEmailMonitoringConfiguration")
    def put_email_monitoring_configuration(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        role_arn: RoleArn,
        log_group_arn: LogGroupArn,
    ) -> PutEmailMonitoringConfigurationResponse:
        raise NotImplementedError

    @handler("PutInboundDmarcSettings")
    def put_inbound_dmarc_settings(
        self, context: RequestContext, organization_id: OrganizationId, enforced: BooleanObject
    ) -> PutInboundDmarcSettingsResponse:
        raise NotImplementedError

    @handler("PutMailboxPermissions")
    def put_mailbox_permissions(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
        grantee_id: WorkMailIdentifier,
        permission_values: PermissionValues,
    ) -> PutMailboxPermissionsResponse:
        raise NotImplementedError

    @handler("PutMobileDeviceAccessOverride")
    def put_mobile_device_access_override(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        user_id: EntityIdentifier,
        device_id: DeviceId,
        effect: MobileDeviceAccessRuleEffect,
        description: MobileDeviceAccessRuleDescription = None,
    ) -> PutMobileDeviceAccessOverrideResponse:
        raise NotImplementedError

    @handler("PutRetentionPolicy")
    def put_retention_policy(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        name: ShortString,
        folder_configurations: FolderConfigurations,
        id: ShortString = None,
        description: PolicyDescription = None,
    ) -> PutRetentionPolicyResponse:
        raise NotImplementedError

    @handler("RegisterMailDomain")
    def register_mail_domain(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        domain_name: WorkMailDomainName,
        client_token: IdempotencyClientToken = None,
    ) -> RegisterMailDomainResponse:
        raise NotImplementedError

    @handler("RegisterToWorkMail")
    def register_to_work_mail(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
        email: EmailAddress,
    ) -> RegisterToWorkMailResponse:
        raise NotImplementedError

    @handler("ResetPassword")
    def reset_password(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        user_id: WorkMailIdentifier,
        password: Password,
    ) -> ResetPasswordResponse:
        raise NotImplementedError

    @handler("StartMailboxExportJob")
    def start_mailbox_export_job(
        self,
        context: RequestContext,
        client_token: IdempotencyClientToken,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
        role_arn: RoleArn,
        kms_key_arn: KmsKeyArn,
        s3_bucket_name: S3BucketName,
        s3_prefix: S3ObjectKey,
        description: Description = None,
    ) -> StartMailboxExportJobResponse:
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: AmazonResourceName, tags: TagList
    ) -> TagResourceResponse:
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: AmazonResourceName, tag_keys: TagKeyList
    ) -> UntagResourceResponse:
        raise NotImplementedError

    @handler("UpdateDefaultMailDomain")
    def update_default_mail_domain(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        domain_name: WorkMailDomainName,
    ) -> UpdateDefaultMailDomainResponse:
        raise NotImplementedError

    @handler("UpdateMailboxQuota")
    def update_mailbox_quota(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        user_id: WorkMailIdentifier,
        mailbox_quota: MailboxQuota,
    ) -> UpdateMailboxQuotaResponse:
        raise NotImplementedError

    @handler("UpdateMobileDeviceAccessRule")
    def update_mobile_device_access_rule(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        mobile_device_access_rule_id: MobileDeviceAccessRuleId,
        name: MobileDeviceAccessRuleName,
        effect: MobileDeviceAccessRuleEffect,
        description: MobileDeviceAccessRuleDescription = None,
        device_types: DeviceTypeList = None,
        not_device_types: DeviceTypeList = None,
        device_models: DeviceModelList = None,
        not_device_models: DeviceModelList = None,
        device_operating_systems: DeviceOperatingSystemList = None,
        not_device_operating_systems: DeviceOperatingSystemList = None,
        device_user_agents: DeviceUserAgentList = None,
        not_device_user_agents: DeviceUserAgentList = None,
    ) -> UpdateMobileDeviceAccessRuleResponse:
        raise NotImplementedError

    @handler("UpdatePrimaryEmailAddress")
    def update_primary_email_address(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        entity_id: WorkMailIdentifier,
        email: EmailAddress,
    ) -> UpdatePrimaryEmailAddressResponse:
        raise NotImplementedError

    @handler("UpdateResource")
    def update_resource(
        self,
        context: RequestContext,
        organization_id: OrganizationId,
        resource_id: ResourceId,
        name: ResourceName = None,
        booking_options: BookingOptions = None,
    ) -> UpdateResourceResponse:
        raise NotImplementedError

