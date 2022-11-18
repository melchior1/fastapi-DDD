import shortuuid
from pydantic import BaseModel

from app.domain.user.user_domain import User as DomainUser, Username, UserLastname, UserEmail, UserId
from app.domain.user.user_repository import UserRepository
from app.infrastructure.user.dto.request_data import UserModel


class CreateUserHandler(BaseModel):
    user_repo: UserRepository

    def execute(self, user_model: UserModel) -> UserId:
        domain_user = DomainUser(
            uuid=UserId(shortuuid.uuid()),
            name=Username(user_model.name),
            lastname=UserLastname(user_model.lastname),
            email=UserEmail(user_model.email)
        )
        try:
            user_id = self.user_repo.create_user(domain_user)
            self.user_repo.commit()
        except Exception:
            self.user_repo.rollback()
            raise
        else:
            return user_id
