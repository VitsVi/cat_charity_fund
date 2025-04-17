from sqlalchemy import Column, Integer, DateTime, Boolean, func, CheckConstraint


class ProjectDonationMixin:
    '''Миксин для расширения таблиц проекта и доната.'''
    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invest_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=func.now())
    close_date = Column(DateTime, nullable=True)

    __tableargs__ = (
        CheckConstraint(
            'full_amount > 0', name='check_full_amount_positive'
        )
    )
