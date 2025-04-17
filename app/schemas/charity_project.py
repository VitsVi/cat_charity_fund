from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class CharityProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=1)
    description: str = Field(..., min_length=1)
    full_amount: int = Field(..., gt=0)




class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectUpdate(CharityProjectBase):
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=1
    )
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[int]


class CharityProjectDB(CharityProjectCreate):
    id: int
    invest_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: datetime

    class Config:
        orm_mode = True