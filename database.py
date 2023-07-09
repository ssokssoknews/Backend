from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DB_URL = 'mysql+pymysql://root:1111@127.0.0.1:3306/SWU_TODAY_NEWS'

engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()