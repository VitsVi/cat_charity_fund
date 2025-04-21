from datetime import datetime as dt
from datetime import timezone as tz

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer


class ProjectDonationMixin:
    """Миксин для расширения таблиц проекта и доната."""

    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=lambda: dt.now(tz.utc))
    close_date = Column(DateTime, nullable=True)

    __tableargs__ = (
        CheckConstraint(
            'full_amount > 0', name='check_full_amount_positive'
        )
    )
