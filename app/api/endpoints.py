from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import (
    create_meme, delete_meme, get_meme_by_id,
    get_meme_id_by_name, update_meme,
    read_all_memes_from_db
)
from app.models import Meme
from app.schemas import MemeBaseCreate, MemeBaseDB, MemeBaseUpdate


router = APIRouter(
    prefix='/memes',
    tags=['Memes']
)


@router.post(
        '/',
        response_model=MemeBaseDB,
        response_model_exclude_none=True,
)
async def create_new_meme(
        meme: MemeBaseCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Создать новый мем"""
    await check_name_duplicate(meme.name, session, meme_id=0)
    new_meme = await create_meme(meme, session)
    return new_meme


@router.patch(
    '/{meme_id}',
    response_model=MemeBaseDB,
    response_model_exclude_none=True,
)
async def partially_update_meme(
        meme_id: int,
        obj_in: MemeBaseUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Частично обновить существующий мем"""
    meme = await check_meme_exists(
        meme_id, session
    )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session, meme_id)
    meme = await update_meme(
        meme, obj_in, session
    )
    return meme


@router.put(
    '/{meme_id}',
    response_model=MemeBaseDB,
    response_model_exclude_none=True,
)
async def fully_update_meme(
    meme_id: int,
    obj_in: MemeBaseUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Полностью обновить существующий мем"""
    meme = await check_meme_exists(
        meme_id, session
    )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session, meme_id)
    meme = await update_meme(
        meme, obj_in, session
    )
    return meme


@router.delete(
    '/{meme_id}',
    response_model=MemeBaseDB,
    response_model_exclude_none=True,
)
async def remove_meme(
    meme_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Удалить существующий мем"""
    meme = await check_meme_exists(
        meme_id, session
    )
    meme = await delete_meme(
        meme, session
    )
    return meme


@router.get(
        '/',
        response_model=list[MemeBaseDB],
        response_model_exclude_none=True,
)
async def get_all_memes(
    session: AsyncSession = Depends(get_async_session),
):
    """Получить список всех мемов"""
    return await read_all_memes_from_db(session)


@router.get(
        '/{meme_id}',
        response_model=MemeBaseDB,
        response_model_exclude_none=True,
)
async def get_meme(
    meme_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Получить конкретный мем по его ID"""
    return await check_meme_exists(
        meme_id, session
    )


async def check_meme_exists(
        meme_id: int,
        session: AsyncSession,
) -> Meme:
    """Корутина, проверяющая существование мема по переданному ID"""
    meme = await get_meme_by_id(
        meme_id, session
    )
    if meme is None:
        raise HTTPException(
            status_code=404,
            detail='Мем не найден!'
        )
    return meme


async def check_name_duplicate(
        meme_name: str,
        session: AsyncSession,
        meme_id: int,
) -> None:
    """Корутина, проверяющая уникальность полученного имени"""
    search_meme_id = await get_meme_id_by_name(meme_name, session)
    if search_meme_id is not None:
        if search_meme_id != meme_id:
            raise HTTPException(
                status_code=422,
                detail='Мем с таким именем уже существует!',
            )
