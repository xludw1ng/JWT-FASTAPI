from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from curso.xludw1ng.fastapi.jwtapi.config.settings import settings

engine = create_engine(settings.BASE_URL, echo=True, pool_recycle=10)
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)
Base = declarative_base()

