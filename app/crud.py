from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import AsyncSessionLocal
from app.models import Meme
from app.schemas import MemeBaseCreate


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

