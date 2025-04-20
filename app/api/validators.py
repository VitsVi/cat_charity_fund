from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud
from app.models import CharityProject
from app.schemas.charity_project import CharityProjectUpdate


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


async def check_project_exists(
        project_id: int,
        session: AsyncSession
) -> CharityProject:
    project = await charity_project_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Проект не найден.'
        )
    return project


async def check_project_donations(
        project_id: int,
        session: AsyncSession
) -> None:
    project = await charity_project_crud.get(project_id, session)
    if project.invested_amount > 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=(
                'Нельзя удалять проект, в '
                'который уже были вложены средства.'
            )
        )


async def update_project_amount_more_than_invested(
        new_data: CharityProjectUpdate,
        old_data: CharityProject,
) -> None:
    if new_data.full_amount < old_data.invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=(
                'Новая требуемая сумма проекта '
                'не может быть меньше уже вложенной суммы.'
            )
        )


async def check_close_project(
        old_data: CharityProject
) -> None:
    if old_data.close_date:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Нельзя изменять/удалять данные закрытого проекта.'
        )
