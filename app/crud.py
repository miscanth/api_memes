from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import AsyncSessionLocal
from app.models import Meme
from app.schemas import MemeBaseCreate, MemeBaseUpdate


async def create_meme(
        new_meme: MemeBaseCreate,
        session: AsyncSession,
) -> Meme:
    new_meme_data = new_meme.dict()
    db_meme = Meme(**new_meme_data)

    session.add(db_meme)
    await session.commit()
    await session.refresh(db_meme)
    return db_meme


async def update_meme(
        db_meme: Meme,
        meme_data_in: MemeBaseUpdate,
        session: AsyncSession,
) -> Meme:
    obj_data = jsonable_encoder(db_meme)
    update_data = meme_data_in.dict(exclude_unset=True)

    for field in obj_data:
        if field in update_data:
            setattr(db_meme, field, update_data[field])
    session.add(db_meme)
    await session.commit()
    await session.refresh(db_meme)
    return db_meme


async def read_all_memes_from_db(
        session: AsyncSession,
) -> list[Meme]:
    db_memes = await session.execute(select(Meme))
    return db_memes.scalars().all()



async def get_meme_id_by_name(
meme_name: str,
session: AsyncSession,
) -> Optional[int]:
    # Получаем объект класса Result.
    db_meme_id = await session.execute(
        select(Meme.id).where(
            Meme.name == meme_name
        )
    )
    # Извлекаем из него конкретное значение.
    return db_meme_id.scalars().first()


async def get_meme_by_id(
meme_id: int,
session: AsyncSession,
) -> Optional[Meme]:
    # Получаем объект класса Result.
    db_meme = await session.execute(
        select(Meme).where(
            Meme.id == meme_id
        )
    )
    # Извлекаем из него конкретное значение.
    return db_meme.scalars().first()