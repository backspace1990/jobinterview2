from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DB_CONNECTION

engine=create_engine(DB_CONNECTION, echo=True)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
