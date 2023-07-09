from fastapi import HTTPException,status
import models,schemas
from sqlalchemy.orm import Session

# 모든 뉴스 get 
def get_all(db:Session):
    swu_news=db.query(models.Swu_news).all()

    if not swu_news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='0 news')

    return swu_news


# 뉴스 기사 등록 
def register(db:Session,request:schemas.Article):
    swu_news=models.Swu_news(title=request.title,content=request.content,url=request.url,published_date=request.published_date,category=request.category,ai_summarize=request.ai_summarize,ai_keyword=request.ai_keyword)
    db.add(swu_news)
    db.commit()
    db.refresh(swu_news)
    return swu_news


# 카테고리별 기사 가져오기
def get_category(db:Session,category:str):
    swu_news=db.query(models.Swu_news).filter(models.Swu_news.category==category).all()
    if not swu_news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'swu news with {category} is not exist')
        
    return swu_news