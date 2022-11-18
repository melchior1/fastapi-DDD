from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.user.user_command_usecase import CreateUserHandler
from app.application.user.user_query_usecase import GetUserById
from app.application.user.user_tranformer import UserTransformer
from app.domain.user.user_repository import UserRepository
from app.infrastructure.db.database import SessionLocal
from app.infrastructure.db.user.user_repository import UseRepositoryImpl


def get_session() -> Iterator[Session]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def user_transformer_dependency() -> UserTransformer:
    return UserTransformer()


def user_repository_dependency(
        session: Session = Depends(get_session),
        user_transformer: UserTransformer = Depends(user_transformer_dependency)
) -> UserRepository:
    return UseRepositoryImpl(user_transformer=user_transformer, session=session)


def create_user_handler_dependency(
        user_repo: UserRepository = Depends(user_repository_dependency)) -> CreateUserHandler:
    return CreateUserHandler(user_repo=user_repo)


def get_user_by_id_handler_dependency(
        user_repo: UserRepository = Depends(user_repository_dependency)) -> GetUserById:
    return GetUserById(user_repo=user_repo)
