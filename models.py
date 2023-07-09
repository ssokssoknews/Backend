from sqlalchemy import Column, TEXT, INT, BIGINT, DATE, String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class User_preference(Base):
#     __tablename__="user_preference"

#     Preference_id=Column(Integer,primary_key=True)
#     user_id=Column(Integer,ForeignKey('users.id'))

#     owner=relationship("User",back_polulates="user_preference")
    
class Preference(Base):
    __tablename__ = "preference"

    preference_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    preference_name = Column(TEXT, nullable=False)


class User(Base):
    __tablename__ = "user"

    user_idx = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(TEXT, nullable=False, primary_key=True)
    user_pwd = Column(String, nullable=False)
    user_name = Column(TEXT, nullable=False)


class User_preference(Base):
    __tablename__ = "user_preference"

    user_idx = Column(INT, nullable=False ,primary_key=True)
    preference_id = Column(INT, nullable=False ,primary_key=True)


class Swu_news(Base):
    __tablename__ = "swu_news"

    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    title = Column(TEXT, nullable=True)
    content = Column(TEXT, nullable=True)
    url = Column(TEXT, nullable=True)
    published_date = Column(DATE, nullable=True)
    category = Column(TEXT, nullable=True)
    ai_summarize = Column(TEXT, nullable=True)
    ai_keyword = Column(TEXT, nullable=True)