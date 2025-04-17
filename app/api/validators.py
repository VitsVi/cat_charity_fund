from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject, Donation, User
from http import HTTPStatus

async def check_project_name_duplicate(
        project_name: str,
        session: AsyncSession
) -> None:
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name, session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail='Проект с таким именем уже существует.'
        )