from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.application.user.user_tranformer import UserTransformer
from app.domain.user.user_domain import User as DomainUser, UserId
from app.domain.user.user_exception import UserNotFoundException
from app.domain.user.user_repository import UserRepository
from app.infrastructure.db.user.user_models import DbUser


class UseRepositoryImpl(UserRepository):
    user_transformer: UserTransformer
    session: Session

    class Config:
        arbitrary_types_allowed = True

    def create_user(self, user_domain: DomainUser) -> UserId:
        db_user = self.user_transformer.from_domain(user_domain)
        self.session.add(db_user)
        return user_domain.uuid

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def fetch_user_by_id(self, user_id: UserId) -> DomainUser:
        try:
            db_user = self.session.query(DbUser).filter_by(uuid=user_id.uuid).one()
        except NoResultFound:
            raise UserNotFoundException from None
        else:
            return self.user_transformer.from_db(db_user)
