from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import create_meme, read_all_memes_from_db
# get_meme_id_by_name
from app.models import Memes
from app.schemas import MemesBaseCreate, MemesBaseDB


router = APIRouter(
    prefix='/memes',
    tags=['Memes']
)


@router.post(
        '/',
        response_model=MemesBaseDB,
        response_model_exclude_none=True,
)
async def create_new_meme(
        meme: MemesBaseCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """meme_id = await get_meme_id_by_name(meme.name, session)
    # Если такой объект уже есть в базе - вызываем ошибку:
    if meme_id is not None:
        raise HTTPException(
            status_code=422,
            detail=' Мем с таким именем уже существует!',
        )"""
    new_meme = await create_meme(meme, session)
    return new_meme


@router.get(
        '/',
        response_model=list[MemesBaseDB],
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