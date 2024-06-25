from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Коллекция мемов'
    app_description: str = 'Приложение предоставляет возможность работать с огромной коллекцией мемов'
    # db_url: str = 'postgres://login:password@127.0.0.1:5432/api_memes'

    class Config:
        env_file = '.env'


settings = Settings()