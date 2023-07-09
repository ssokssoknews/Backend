from fastapi import APIRouter, Depends, HTTPException,status
import models,schemas,database
from sqlalchemy.orm import Session
from typing import List
from aiNewsModel import generate_summary
from repository import user,news
from hashing import Hash
import JWTtoken
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.user_id==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'invalid credentials')
    if not Hash.verify(user.user_pwd,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Incorrect password')
    
    #access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = JWTtoken.create_access_token(
        data={"sub": user.user_id}#schemas.User.user_id} #, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}