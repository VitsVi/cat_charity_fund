from app.services.investment import investment
from app.crud import charity_project_crud
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.charity_project import (
    CharityProjectCreate, CharityProjectUpdate
)
from app.models import CharityProject
from app.api.validators import update_project_full_invested


async def create_charity_project_logic(
    project: CharityProjectCreate,
    session: AsyncSession
):

    new_project = await charity_project_crud.create(project, session)
    await investment.main(new_project, session)
    await session.refresh(new_project)
    return new_project


async def update_charity_project_logic(
    project: CharityProject,
    obj_in: CharityProjectUpdate,
    session: AsyncSession
):
    if obj_in.full_amount is not None:
        project = await update_project_full_invested(project, obj_in)
    project = await charity_project_crud.update(
        project, obj_in, session
    )
    return project
