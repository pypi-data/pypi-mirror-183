from enum import Enum
from typing import TypeVar, Generic, Optional
from pydantic import BaseModel


class ActionStatus(str, Enum):
    """
    Action status.
    """
    success = "success"
    failure = "failure"


T = TypeVar("T")


class Result(BaseModel, Generic[T]):
    """

    """
    status: ActionStatus
    data: Optional[T]
    error: Optional[str]

    class Config:
        use_enum_values = True

    def is_success(self):
        return self.status == ActionStatus.success

    def is_failure(self):
        return not self.is_success()

    @classmethod
    def success(cls, data: Optional[T] = None):
        return Result(status=ActionStatus.success, data=data, error=None)

    @classmethod
    def failure(cls, error: str):
        return Result(status=ActionStatus.failure, data=None, error=error)

    @classmethod
    def server_error(
        cls,
        error: str = "An error occurred while performing the operation. please try again late or contact support.",
    ):
        return Result(status=ActionStatus.failure, data=None, error=error)


