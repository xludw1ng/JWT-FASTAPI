from typing import List

from sqlalchemy.orm import Session

from curso.xludw1ng.fastapi.jwtapi.entities.users import User as UserEntity
from curso.xludw1ng.fastapi.jwtapi.repositories.user_repository import UserRepository
from curso.xludw1ng.fastapi.jwtapi.schemas.user_dto import UserDto
from curso.xludw1ng.fastapi.jwtapi.schemas.user_request import UserRequest
from curso.xludw1ng.fastapi.jwtapi.security.passwords import hash_password
from curso.xludw1ng.fastapi.jwtapi.services.user_service import UserService


class UserServiceImpl(UserService):
    def __init__(self, repo: UserRepository, db: Session):
        self._db = db
        self._repo = repo

    def find_all(self) -> List[UserDto]:
        return [UserDto.model_validate(user) for user in self._repo.find_all()]

    def find_by_id(self, user_id: int) -> UserDto | None:
        user = self._repo.find_by_id(user_id)
        if not user:
            return None
        return UserDto.model_validate(user)

    def find_by_email(self, email: str) -> UserDto | None:
        user = self._repo.find_by_email(email)
        if not user:
            return None
        return UserDto.model_validate(user)

    def create(self, user: UserRequest) -> UserDto:
        if self._repo.find_by_email(user.email):
            raise ValueError('Email already registered')

        password_hash = hash_password(user.password)
        user_entity = UserEntity(email=user.email, password=password_hash)
        try:
            self._db.add(user_entity)
            self._db.commit()
            self._db.refresh(user_entity)
            return UserDto.model_validate(user_entity)
        except Exception:
            self._db.rollback()
            raise