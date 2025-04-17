from typing import Optional
from pydantic import Field, BaseModel
from datetime import datetime


class DonationBase(BaseModel):
    comment: Optional[str]
    full_amount: int = Field(..., gt=0)


class DonationCreate(DonationBase):
    pass


class DonationUserDB(DonationBase):
    id: int
    create_date: datetime


    class Config:
        orm_mode = True


class DonationAdminDB(DonationBase):
    id: int
    invest_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: datetime


    class Config:
        orm_mode = True