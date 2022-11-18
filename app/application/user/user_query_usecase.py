from pydantic import BaseModel

from app.domain.user.user_domain import User as DomainUser, UserId
from app.domain.user.user_repository import UserRepository


class GetUserById(BaseModel):
    user_repo: UserRepository

    def execute(self, user_id: UserId) -> DomainUser:
        try:
            user_domain = self.user_repo.fetch_user_by_id(user_id)
        except Exception:
            raise
        else:
            return user_domain
