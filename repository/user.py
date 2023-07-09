from fastapi import HTTPException,status
import models,schemas
from hashing import Hash

def login(db,user_id,user_pwd):
    user=db.query(models.User).filter(models.User.user_id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user {user_id} is not exist')

    if user_pwd!=user.user_pwd:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f'Invalid password')
    return user


def create(db,request:schemas.User):
    user=db.query(models.User).filter(models.User.user_id==request.user_id).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user already exist")
  
    new_user=models.User(user_id=request.user_id,user_pwd=Hash.bcrypt(request.user_pwd),user_name=request.user_name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def withdrawal(db,user_id):
    user=db.query(models.User).filter(models.User.user_id==user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user not exist")
    user.delete(synchronize_session=False)
    db.commit()
    return {'msg':'successfully withdraw'}


def update(db,id,request:schemas.User):
    user = db.query(models.User).filter(models.User.user_id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user not exist")
    user.update({'user_id':request.user_id},synchronize_session=False)
    db.commit()
    return {'msg':'updated successfully'}