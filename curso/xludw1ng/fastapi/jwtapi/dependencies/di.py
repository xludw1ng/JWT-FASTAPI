from fastapi import Depends
from sqlalchemy.orm import Session

from curso.xludw1ng.fastapi.jwtapi.config.db import SessionLocal
from curso.xludw1ng.fastapi.jwtapi.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from curso.xludw1ng.fastapi.jwtapi.repositories.user_repository import UserRepository
from curso.xludw1ng.fastapi.jwtapi.services.user_service import UserService
from curso.xludw1ng.fastapi.jwtapi.services.user_service_impl import UserServiceImpl

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_repository(db: Session = Depends(get_db)) -> UserRepository:
    return SQLAlchemyUserRepository(db)

def get_service(db : Session = Depends(get_db), repo: UserRepository = Depends(get_repository)) -> UserService:
    return UserServiceImpl(repo, db)

