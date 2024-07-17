from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.core.db import Base, engine


class Memes(Base):

    meme_text = Column(String(100), index=True)

