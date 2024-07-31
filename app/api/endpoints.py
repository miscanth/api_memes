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
    await check_name_duplicate(meme.name, 0, session)
    new_meme = await create_meme(meme, session)
    return new_meme


@router.patch(
    # ID обновляемого объекта будет передаваться path-параметром.
    '/{meme_id}',
    response_model=MemeBaseDB,
    response_model_exclude_none=True,
)
async def partially_update_meme(
        # ID обновляемого объекта.
        meme_id: int,
        # JSON-данные, отправленные пользователем.
        obj_in: MemeBaseUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    # Получаем объект из БД по ID.
    # В ответ ожидается либо None, либо объект класса Meme
    meme = await get_meme_by_id(
        meme_id, session
    )

    if meme is None:
        raise HTTPException(
            status_code=404, 
            detail='Мем не найден!'
        )

    if obj_in.name is not None:
        # Если в запросе получено поле name — проверяем его на уникальность.
        await check_name_duplicate(obj_in.name, meme_id, session)

    # Передаём в корутину все необходимые для обновления данные.
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
    meme = await get_meme_by_id(
        meme_id, session
    )
    if meme is None:
        raise HTTPException(
            status_code=404, 
            detail='Мем не найден!'
        )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, meme_id, session)
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
    meme = await get_meme_by_id(
        meme_id, session
    )
    if meme is None:
        raise HTTPException(
            status_code=404, 
            detail='Мем не найден!'
        )
    meme = await delete_meme(
        meme, session
    )
    return meme


# Корутина, проверяющая уникальность полученного имени.
async def check_name_duplicate(
        meme_name: str,
        meme_id: int,
        session: AsyncSession,
) -> None:
    search_meme_id = await get_meme_id_by_name(meme_name, session)
    if search_meme_id is not None:
        if search_meme_id != meme_id:
            raise HTTPException(
                status_code=422,
                detail='Мем с таким именем уже существует!',
            ) 


@router.get(
        '/',
        response_model=list[MemeBaseDB],
        response_model_exclude_none=True,
)
async def get_all_memes(
    session: AsyncSession = Depends(get_async_session),
):
    return await read_all_memes_from_db(session)




"""@router.get('/memes', response_model=list[MemesBase], status_code=status.HTTP_200_OK)
def get_all_memes():
    #Получить список всех мемов
    return db.query(Memes).all()


@router.get('/memes/{meme_id}', response_model=MemesBase, status_code=status.HTTP_200_OK)
def get_meme(meme_id: int):
    #Получить конкретный мем по его ID
    meme = db.query(Memes).filter(Memes.id==meme_id).first()
    if meme is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meme with this id doesn't exist!")
    return meme


@router.post('/memes', response_model=MemesBase, status_code=status.HTTP_201_CREATED)
def create_meme(meme: MemesBase):
    # Добавить новый мем
    new_meme = Memes(
        id = meme.id,
        meme_text = meme.meme_text,
    )
    find_meme_id = db.query(Memes).filter(Memes.id==meme.id).first()
    if find_meme_id is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Meme with this id is already exists!")
    db.add(new_meme)
    db.commit()
    db.refresh(new_meme)
    return new_meme


@router.put('/memes/{meme_id}', response_model=MemesBase, status_code=status.HTTP_202_ACCEPTED)
def edit_meme(meme_id: int, meme: MemesBase):
    # Обновить существующий мем
    edited_meme = db.query(Memes).filter(Memes.id==meme_id).first()
    if edited_meme is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meme with this id doesn't exist!")
    edited_meme.meme_text = meme.meme_text
    
    db.commit()
    db.refresh(edited_meme)
    return edited_meme


@router.delete('/memes/{meme_id}', response_model=MemesBase, status_code=status.HTTP_200_OK)
def delete_meme(meme_id: int):
    # Удалить мем
    meme_to_delete = db.query(Memes).filter(Memes.id==meme_id).first()
    if meme_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meme with this id doesn't exist!")

    db.delete(meme_to_delete)
    db.commit()
    return meme_to_delete"""