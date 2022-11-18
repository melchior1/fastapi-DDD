from abc import ABC, abstractmethod

from pydantic import BaseModel

from app.domain.user.user_domain import User as DomainUser, UserId


class UserRepository(ABC, BaseModel):
    @abstractmethod
    def create_user(self, user_domain: DomainUser) -> UserId:
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    def fetch_user_by_id(self, user_id: UserId) -> DomainUser:
        pass
