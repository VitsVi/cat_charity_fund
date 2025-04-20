from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Название'
    app_description: str = 'Описание'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
