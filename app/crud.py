from typing import Optional

from sqlalchemy import select

from app.core.db import AsyncSessionLocal
from app.models import Memes
from app.schemas import MemesBase


async def create_meme(
        new_meme: MemesBase
) -> Memes:
    new_meme_data = new_meme.dict()

    # Создаём объект модели Memes.
    # В параметры передаём пары "ключ=значение", для этого распаковываем словарь.
    db_meme = Memes(**new_meme_data)

    # Создаём асинхронную сессию через контекстный менеджер.
    async with AsyncSessionLocal() as session:
        # Добавляем созданный объект в сессию. 
        # Никакие действия с базой пока ещё не выполняются.
        session.add(db_meme)

        # Записываем изменения непосредственно в БД. 
        # Так как сессия асинхронная, используем ключевое слово await.
        await session.commit()

        # Обновляем объект db_room: считываем данные из БД, чтобы получить его id.
        await session.refresh(db_meme)
    # Возвращаем только что созданный объект класса MeetingRoom.
    return db_meme


async def read_all_memes_from_db(
        #session: AsyncSession,
) -> list[Memes]:
    async with AsyncSessionLocal() as session:
        db_memes = await session.execute(select(Memes))
    return db_memes.scalars().all()



"""async def get_meme_id_by_name(meme_name: str) -> Optional[int]:
    async with AsyncSessionLocal() as session:
        # Получаем объект класса Result.
        db_meme_id = await session.execute(
            select(Memes.id).where(
                Memes.name == meme_name
            )
        )
        # Извлекаем из него конкретное значение.
        return db_meme_id.scalars().first()"""

