from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core import Base
from app.models.project_donation_mixin import ProjectDonationMixin


class Donation(ProjectDonationMixin, Base):
    """Модель таблицы пожертвований в фонде."""

    user_id = Column(Integer, ForeignKey(
        'user.id', name='fk_donation_user_id'
    ), nullable=False)
    comment = Column(Text, nullable=True)
