from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class CharityProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: int

    @field_validator('full_amount')
    def check_amount_more_zero(self, value):
        if value < 1:
            raise ValueError('Требуемая сумма сбора должна быть больше 0.')
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "name": 'Название проекта',
                "description": 'Описание проекта',
                "full_amount": 100000
            }
        }


class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectUpdate(CharityProjectBase):
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100
    )
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[int]


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
