from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_close_project, check_project_donations,
                                check_project_exists,
                                check_project_name_duplicate,
                                update_project_amount_more_than_invested)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud import charity_project_crud
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.services.investment import investment

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def create_new_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session)
):
    """Создание новых проектов в фонде, только для админа."""
    await check_project_name_duplicate(project.name, session)
    new_project = await charity_project_crud.create(project, session)
    await investment.main(new_project, session)
    await session.refresh(new_project)
    return new_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_projects(
    session: AsyncSession = Depends(get_async_session)
):
    """Просмотр всех проектов в фонде, без ограничений."""
    all_projects = await charity_project_crud.get_multi(session)
    return all_projects


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def partially_update_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    """Изменение полей проекта."""
    project = await check_project_exists(project_id, session)

    if obj_in.name is not None:
        await check_project_name_duplicate(obj_in.name, session)

    await check_close_project(project)  # Проверка закрытого проекта.

    # Проверка валидности требуемой суммы проекта.
    await update_project_amount_more_than_invested(project, obj_in)

    project = await charity_project_crud.update(
        project, obj_in, session
    )
    return project


@router.delete(
    '/{project_id}',
    dependencies=[Depends(current_superuser)]
)
async def remove_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """Удаление проекта."""
    project = await check_project_exists(project_id, session)
    # Проверка наличия пожертвований в проекте.
    await check_project_donations(project_id, session)

    await check_close_project(project)  # Проверка закрытого проекта.
    project = await charity_project_crud.remove(project, session)
    return project