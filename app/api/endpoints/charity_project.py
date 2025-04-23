from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_close_project, check_project_donations,
                                check_project_exists,
                                check_project_name_duplicate)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud import charity_project_crud
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.services.charity_project import (
    create_charity_project_logic,
    update_charity_project_logic
)

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
    return await create_charity_project_logic(project, session)


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
    return await update_charity_project_logic(project, obj_in, session)


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