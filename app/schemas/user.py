from fastapi_users.schemas import BaseUser


class UserRead(BaseUser[int]):
    pass


class UserCreate(BaseUser[int]):
    pass


class UserUpdate(BaseUser[int]):
    pass