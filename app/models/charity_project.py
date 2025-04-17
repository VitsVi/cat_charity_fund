from sqlalchemy import Column, Text, String
from app.core import Base
from app.models.project_donation_mixin import ProjectDonationMixin

class CharityProject(ProjectDonationMixin, Base):
    '''Модель таблицы проектов в фонде.'''
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)
