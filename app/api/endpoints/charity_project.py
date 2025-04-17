from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.crud import charity_project_crud
from app.models import CharityProject
from app.schemas.charity_project import(
    CharityProjectCreate,
    CharityProjectUpdate,
    CharityProjectDB
)
from app.core.user import current_user, current_superuser
from app.api.validators import check_project_name_duplicate


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
    '''Создание новых проектов в фонде, только для админа.'''
    await check_project_name_duplicate(project.name, session)
    new_project = await charity_project_crud.create(project, session)
    return new_project