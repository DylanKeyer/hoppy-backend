from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(f'postgres://chykvgsx:BUWxDzq9_BIV_GKOn6Bzc56hFG6Oy19N@baasu.db.elephantsql.com:5432/chykvgsx')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
    id = Column(Integer, primary_key=True)
    created_dtm = Column(DateTime)
    updated_dtm = Column(DateTime)

