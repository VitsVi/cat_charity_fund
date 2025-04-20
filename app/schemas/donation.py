from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class DonationBase(BaseModel):
    comment: Optional[str]
    full_amount: int = Field(..., gt=0)

    @field_validator('full_amount')
    def check_amount_more_zero(cls, value):
        if value < 1:
            raise ValueError('Требуемая сумма сбора должна быть больше 0.')
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "comment": 'Сообщение к пожертвованию.',
                "full_amount": 1000
            }
        }


class DonationCreate(DonationBase):
    pass


class DonationUserDB(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationAdminDB(DonationBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: datetime

    class Config:
        orm_mode = True
