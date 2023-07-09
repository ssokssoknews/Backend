from pydantic import BaseModel
import datetime
from typing import Optional, List
from typing import Union

class Article(BaseModel):
    title:str 
    content:str 
    url:str 
    published_date:Optional[datetime.date]
    category:Optional[str]
    ai_summarize:Optional[str]
    ai_keyword:Optional[str]


class ShowArticle(BaseModel):
    title:str  
    url:str 
    published_date:Optional[datetime.date]
    category:Optional[str]
    ai_summarize:Optional[str]
    class Config():
        orm_mode=True

class User(BaseModel):
    user_id:str
    user_pwd:str
    user_name:str


class ShowUser(BaseModel):
    user_id:str
    user_name:str 
    class Config():
        orm_mode=True


class Login(BaseModel):
    user_id:str
    user_pwd:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[str] = None