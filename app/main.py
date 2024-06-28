from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

from app.core.config import settings
from app.models import Memes
from app.core.db import engine, SessionLocal
from sqlalchemy.orm import Session
from app.core.db import Base


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)

Base.metadata.create_all(bind=engine)


# pydentic model
class MemesBase(BaseModel):
    id: int
    meme_text: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


"""@app.post('/memes/')
async def create_memes(meme: MemesBase, db: db_dependency):
    db_meme = Memes(meme_text=meme.meme_text)
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
"""


@app.get('/')
def read_root():
    return {'Hello': 'FastAPI'} 

@app.get('/{name}')
def greetings(name):
    return {'Hello': name}

@app.post('/memes', status_code=200)
async def create_memes(meme: MemesBase):
    # return meme.meme_text
    return {
        'id': meme.id,
        'meme_text': meme.meme_text,
    }