from typing import Optional

from pydantic import BaseModel, Field


"""class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True"""


class MemeBase(BaseModel):
    name : Optional[str] = Field(None, min_length=1, max_length=40)
    meme_text: Optional[str] = Field(None, min_length=5, max_length=100)


class MemeBaseCreate(MemeBase):
    name: str = Field(..., min_length=1, max_length=40)


class MemeBaseUpdate(MemeBase):
    pass


class MemeBaseDB(MemeBaseCreate):
    id: int

    class Config:
        orm_mode = True 
