from fastapi import APIRouter
from app.schemas.donation import DonationAdminDB, DonationUserDB, DonationCreate
from fastapi import Depends
from app.core.user import current_user, current_superuser
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.crud import donation_crud
from app.models import Donation, User


router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationAdminDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def get_all_donations_by_admin(
    session: AsyncSession = Depends(get_async_session)
):
    donations = await donation_crud.get_multi(session)
    return donations


@router.get(
    '/my',
    response_model=list[DonationUserDB],
    response_model_exclude_none=True
)
async def get_user_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    donations = await donation_crud.get_donations_by_user(user.id, session)
    return donations


@router.post(
    '/',
    response_model=DonationUserDB,
    response_model_exclude_none=True,
)
async def create_donation(
    donation_obj: DonationCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    donation = await donation_crud.create(donation_obj, session=session, user=user)
    return donation