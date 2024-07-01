from fastapi import FastAPI
from app.core.config import settings
from app.core.db import engine
from app.core.db import Base

from app.api.endpoints import router


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)

app.include_router(router)

Base.metadata.create_all(bind=engine)
