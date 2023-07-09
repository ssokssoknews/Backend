from fastapi import APIRouter, Depends, HTTPException,status
import models,schemas,database,oauth2
from sqlalchemy.orm import Session
from typing import List
from repository import user

router = APIRouter(
    prefix='/user',
    tags=['User']
)

get_db=database.get_db

# 로그인
# @router.get("/signin/{user_id}/{user_pwd}",response_model=schemas.ShowUser,status_code=status.HTTP_200_OK)
# async def user_sign_in(user_id,user_pwd,db:Session=Depends(get_db)):
#     return user.login(db,user_id,user_pwd)


# 회원 가입 
@router.post("/join", response_model=schemas.ShowUser , status_code=status.HTTP_201_CREATED)
async def user_join(request:schemas.User,db:Session=Depends(get_db)):
    #hashedPassword=pwd_context.hash(request.user_pwd)
    
    return user.create(db,request)



# 회원탈퇴
@router.delete("/withdrawal/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
async def MMBRS_WTHDR(user_id,db:Session=Depends(get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
    return user.withdrawal(db,user_id)


# update id
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update_prac(id,request:schemas.User,db:Session=Depends(get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
    return user.update(db,id,request)