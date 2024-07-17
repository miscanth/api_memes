from typing import Optional

from pydantic import BaseModel, Field


"""class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True"""


class MemesBase(BaseModel):
    meme_text: Optional[str] = Field(None, min_length=5, max_length=100)
    # description: Optional[str]


class MemesBaseCreate(MemesBase):
    meme_text: str = Field(..., min_length=5, max_length=100)


class MemesBaseDB(MemesBaseCreate):
    id: int

    class Config:
        orm_mode = True 
