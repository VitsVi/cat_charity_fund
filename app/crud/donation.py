from app.crud.base import CRUDBase
from app.models import Donation
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from sqlalchemy import select

class DonationCRUD(CRUDBase):
    
    async def get_donations_by_user(
            self,
            user_id: int,
            session: AsyncSession
    ):
        donations = await session.execute(
            select(self.model).where(self.model.user_id == user_id)
        )
        return donations.scalars().all()

donation_crud = DonationCRUD(Donation)