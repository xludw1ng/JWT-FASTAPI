from abc import ABC, abstractmethod
from typing import List

from sqlalchemy.orm import Session

from curso.xludw1ng.fastapi.jwtapi.repositories.user_repository import UserRepository
from curso.xludw1ng.fastapi.jwtapi.schemas.user_dto import UserDto
from curso.xludw1ng.fastapi.jwtapi.schemas.user_request import UserRequest


class UserService(ABC):

    @abstractmethod
    def find_all(self) -> List[UserDto]:
        ...


    @abstractmethod
    def find_by_id(self, user_id: int) -> UserDto | None:
        ...


    @abstractmethod
    def find_by_email(self, email: str) -> UserDto | None:
        ...


    @abstractmethod
    def create(self, user: UserRequest) -> UserDto:
        ...