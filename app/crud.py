from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import AsyncSessionLocal
from app.models import Memes
from app.schemas import MemesBase


async def create_meme(
        new_meme: MemesBase,
        session: AsyncSession,
) -> Memes:
    new_meme_data = new_meme.dict()
    db_meme = Memes(**new_meme_data)

    session.add(db_meme)
    await session.commit()
    await session.refresh(db_meme)
    return db_meme


async def read_all_memes_from_db(
        session: AsyncSession,
) -> list[Memes]:
    db_memes = await session.execute(select(Memes))
    return db_memes.scalars().all()



"""async def get_meme_id_by_name(
meme_name: str,
session: AsyncSession,
) -> Optional[int]:
    # Получаем объект класса Result.
    db_meme_id = await session.execute(
        select(Memes.id).where(
            Memes.name == meme_name
        )
    )
    # Извлекаем из него конкретное значение.
    return db_meme_id.scalars().first()"""

