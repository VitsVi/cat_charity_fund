from app.services.investment import investment
from app.crud import donation_crud
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.donation import DonationCreate
from app.models import User


async def create_donation_logic(
    donation_obj: DonationCreate,
    session: AsyncSession,
    user: User
):
    donation = await donation_crud.create(
        donation_obj, session=session, user=user
    )
    await investment.main(donation, session)
    await session.refresh(donation)
    return donation
