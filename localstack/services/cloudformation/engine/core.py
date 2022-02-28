import dataclasses
import datetime
from enum import Enum
from typing import List

# subclasses

@dataclasses.dataclass
class Resource:
    pass

@dataclasses.dataclass
class Parameter:
    pass

class ChangeSetExecutionStatus(Enum):
    AVAILABLE = 1
    UNAVAILABLE = 2
    OBSOLETE = 3

class ChangeSetStatus(Enum):
    CREATE_IN_PROGRESS = 1
    CREATE_COMPLETE = 2
    FAILED = 3


# entities with full lifecycles


@dataclasses.dataclass
class Stack:
    stack_name: str
    template: str  # TODO



@dataclasses.dataclass(frozen=True)
class ChangeSet:
    change_set_id: str
    change_set_name: str
    stack_id: str
    stack_name: str

    description: str
    parameters: List[Parameter]
    creation_time: datetime.datetime
    execution_status: ChangeSetExecutionStatus
    status: ChangeSetStatus
    status_reason: str


    pass

# @dataclasses.dataclass
# class StackSet:
#     pass
#
# @dataclasses.dataclass
# class StackInstance:
#     pass



# state related

@dataclasses.dataclass
class ResourceChange:
    pass

@dataclasses.dataclass
class StackEvent:
    pass

