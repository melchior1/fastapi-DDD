from fastapi import APIRouter, Query

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get('/{uuid}')
def get_by_uuid(uuid: str):
    """
    will return the user from provided uuid.

    uuid: uuid of the user
    """
    return {'message', f'get user by uuid: {uuid}'}


@router.get('/list')
def get_all_user(
        current_page: int = Query(1, alias='currentPage'),
        item_per_page: int = Query(10, alias="itemPerPage")
):
    """
    will return list of paginated user
    """
    return {f'list of user on page {current_page}, total : {item_per_page}'}
