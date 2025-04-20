from datetime import datetime as dt
from datetime import timezone as tz
from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


class Investment:

    def __init__(self):
        self.projects: list[CharityProject] = []
        self.donations: list[Donation] = []

    async def get_open_donations(
            self,
            session: AsyncSession
    ):
        donations = await session.execute(
            select(Donation)
            .where(Donation.fully_invested is False)
            .order_by(Donation.create_date)
        )
        self.donations = donations.scalars().all()

    async def get_open_projects(
            self,
            session: AsyncSession
    ):
        projects = await session.execute(
            select(CharityProject)
            .where(CharityProject.fully_invested is False)
            .order_by(CharityProject.create_date)
        )
        self.projects = projects.scalars().all()

    async def add_new_object(
            self,
            obj,
    ):
        if isinstance(obj, CharityProject):
            self.projects.append(obj)
        elif isinstance(obj, Donation):
            self.donations.append(obj)

    async def investition(self):
        for project in self.projects:
            for donation in self.donations:

                invest_remain = donation.full_amount - donation.invested_amount
                project_need_invest = \
                    project.full_amount - project.invested_amount

                invest_amount = min(invest_remain, project_need_invest)

                project.invested_amount += invest_amount
                donation.invested_amount += invest_amount

                if donation.full_amount == donation.invested_amount:
                    donation.fully_invested = True
                    donation.close_date = dt.now(tz.utc)

                elif project.full_amount == project.invested_amount:
                    project.fully_invested = True
                    project.close_date = dt.now(tz.utc)
                    break

    async def commit_investitions(
        self,
        session: AsyncSession
    ):
        session.add_all(self.projects + self.donations)
        await session.commit()

    async def main(
            self,
            object: Union[CharityProject, Donation],
            session: AsyncSession
    ):
        await self.get_open_donations(session)
        await self.get_open_projects(session)
        await self.add_new_object(object)
        await self.investition()
        await self.commit_investitions(session)


investment = Investment()
