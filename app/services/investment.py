from app.models import CharityProject, Donation
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

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
            .where(Donation.fully_invested==False)
            .order_by(Donation.create_date)
        )
        self.donations = donations.scalars().all()


    async def get_open_projects(
            self,
            session: AsyncSession
    ):
        projects = await session.execute(
            select(CharityProject)
            .where(CharityProject.fully_invested==False)
            .order_by(CharityProject.create_date)
        )
        self.projects = projects.scalars().all()


    async def new_object_add(
            self,
            obj,
    ):
        if isinstance(obj, CharityProject):
            self.projects.append(obj)
        elif isinstance(obj, Donation):
            self.donations.append(obj)


    async def investition(self):
        ...


    async def commit_investitions(
        self,
        session: AsyncSession
    ):
        session.add_all(self.projects + self.donations)
        await session.refresh()
        await session.commit()


    async def main(
            self,
            object: CharityProject | Donation,
            session: AsyncSession
    ):
        self.get_open_donations(session)
        self.get_open_projects(session)
        self.new_object_add(object)
        self.investition()
        self.commit_investitions(session)

investment = Investment()