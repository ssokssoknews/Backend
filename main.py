from fastapi import FastAPI
from pydantic import BaseModel
from database import engine
import models
from routers import user,news,authentication

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(news.router)
app.include_router(authentication.router)

