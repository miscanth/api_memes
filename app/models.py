from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.core.db import Base, engine


class Meme(Base):

    name = Column(String(40), unique=True, nullable=False)
    meme_text = Column(String(100), index=True)

