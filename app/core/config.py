from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    app_title: str = 'Коллекция мемов'
    app_description: str = 'Приложение предоставляет возможность работать с огромной коллекцией мемов'
    database_url: str


    class Config:
        env_file = '.env'


settings = Settings()