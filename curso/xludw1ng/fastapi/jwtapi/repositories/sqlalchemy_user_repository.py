from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from curso.xludw1ng.fastapi.jwtapi.entities.users import User as UserEntity
from curso.xludw1ng.fastapi.jwtapi.repositories.user_repository import UserRepository


class SQLAlchemyUserRepository(UserRepository):

    def __init__(self, db: Session):
        self._db = db


    def find_all(self) -> List[UserEntity]:
        stmt = select(UserEntity).order_by(UserEntity.id.asc())
        return list(self._db.scalars(stmt).all())

    def find_by_id(self, user_id: int) -> Optional[UserEntity]:
        return self._db.get(UserEntity, user_id)


    def find_by_email(self, email: str) -> Optional[UserEntity]:
        stmt = select(UserEntity).where(UserEntity.email == email)
        return self._db.scalar(stmt)


    def create(self, user: UserEntity) -> UserEntity:
        self._db.add(user)
        return user
