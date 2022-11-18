from pydantic import BaseModel

from app.domain.user.user_domain import User as DomainUser, Username, UserLastname, UserEmail, UserId
from app.infrastructure.db.user.user_models import DbUser


class UserTransformer(BaseModel):
    @staticmethod
    def from_domain(domain_user: DomainUser) -> DbUser:
        return DbUser(
            uuid=domain_user.uuid.uuid,
            name=domain_user.name.name,
            lastname=domain_user.lastname.lastname,
            email=domain_user.email.email
        )

    @staticmethod
    def from_db(db_user: DbUser) -> DomainUser:
        return DomainUser(
            uuid=UserId(db_user.uuid),
            name=Username(db_user.name),
            lastname=UserLastname(db_user.lastname),
            email=UserEmail(db_user.email)
        )
