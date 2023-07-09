from fastapi import APIRouter, Depends, HTTPException,status
import models,schemas,database
from sqlalchemy.orm import Session
from typing import List
from aiNewsModel import generate_summary
from repository import user,news

router = APIRouter(
    prefix='/news',
    tags=['news']
)

get_db=database.get_db

# 모든 뉴스 get 
@router.get("/",response_model=List[schemas.ShowArticle],status_code=status.HTTP_200_OK)
async def fetch_swu_news(db:Session=Depends(get_db)):
    return news.get_all(db)


# 뉴스 기사 등록 
@router.post("/" , status_code=status.HTTP_201_CREATED)
async def register_article(request:schemas.Article,db:Session=Depends(get_db)):
    return news.register(db,request)
     

 # 카테고리 별 뉴스 get
@router.get("/{category}",status_code=status.HTTP_200_OK)
async def fetch_category_news(category,db:Session=Depends(get_db)):
    return news.get_category(db,category)


# 요약 모델 호출
@router.get('/summarize/{news}')
async def call_model(news):
    output=generate_summary(news)
    return output 