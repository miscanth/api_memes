from pydantic import BaseModel


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class MemesBase(OurBaseModel):
    id: int
    meme_text: str
