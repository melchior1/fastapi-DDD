from fastapi import APIRouter, Body, Depends

from app.application.user.user_command_usecase import CreateUserHandler
from app.application.user.user_query_usecase import GetUserById
from app.dependency_injections import create_user_handler_dependency, get_user_by_id_handler_dependency
from app.infrastructure.user.dto.request_data import UserModel

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/create')
def create_user(
        user_model: UserModel = Body(embed=True, alias='user'),
        create_user_handler: CreateUserHandler = Depends(create_user_handler_dependency),
        get_user_by_id_handler: GetUserById = Depends(get_user_by_id_handler_dependency)
):
    user_id = create_user_handler.execute(user_model)
    return get_user_by_id_handler.execute(user_id).toJson()
