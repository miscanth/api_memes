from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, declared_attr
#from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings


class PreBase:

    @declared_attr  
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)
# Base = declarative_base()

engine = create_async_engine(settings.database_url)
#engine = create_engine(settings.database_url, echo=True)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#db = SessionLocal()

"""async def get_async_session():
    # Асинхронный генератор сессий
    async with AsyncSessionLocal() as async_session:
        yield async_session"""