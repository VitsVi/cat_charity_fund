from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject
from app.schemas.charity_project import CharityProjectUpdate

class CharityProjectCRUD(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject).where(
                CharityProject.name == project_name
            )
        )
        return db_project_id.scalars().first()


charity_project_crud = CharityProjectCRUD(CharityProject)