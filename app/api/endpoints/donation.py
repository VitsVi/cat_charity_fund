from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud import donation_crud
from app.models import User
from app.schemas.donation import (DonationAdminDB, DonationCreate,
                                  DonationUserDB)
from app.services.donation import create_donation_logic


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
    return await create_donation_logic(donation_obj, session, user)
