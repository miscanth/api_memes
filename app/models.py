from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.core.db import Base, engine


"""class Meme(Base):
    # Имя для мема должно быть не больше 100 символов,
    # уникальным и непустым.
    name = Column(String(100), unique=True, nullable=False) """


class Memes(Base):
    __tablename__ = 'memes'

    id = Column(Integer, primary_key=True, index=True)
    meme_text = Column(String(20), index=True)


"""class Choices(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('questions.id'))"""

def create_tables():
    Base.metadata.create_all(bind=engine)

def drop_tables():
    Base.metadata.drop_all(bind=engine)