import re

from pydantic import BaseModel
from pydantic.dataclasses import dataclass

from app.domain.user.user_exception import InvalidUserNameException, InvalidUserLastnameException


@dataclass(frozen=True)
class UserId(BaseModel):
    uuid: str


@dataclass(frozen=True)
class Username(BaseModel):
    name: str

    def __post_init__(self):
        self.validate_name(self.name)

    @staticmethod
    def validate_name(name: str):
        if len(name) > 10:
            raise InvalidUserNameException


@dataclass(frozen=True)
class UserLastname(BaseModel):
    lastname: str

    def __post_init__(self):
        self.validate_name(self.lastname)

    @staticmethod
    def validate_name(lastname: str):
        if 20 < len(lastname) < 2:
            raise InvalidUserLastnameException


@dataclass(frozen=True)
class UserEmail(BaseModel):
    email: str

    def __post_init__(self):
        pass

    def validate_email(self):
        if not re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.email):
            raise InvalidUserNameException


class User(BaseModel):
    uuid: UserId
    name: Username
    lastname: UserLastname
    email: UserEmail

    def toJson(self) -> dict[str, str]:
        return {
            "uuid": self.uuid.uuid,
            "name": self.name.name,
            "lastname": self.lastname.lastname,
            "email": self.email.email
        }
