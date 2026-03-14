from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError

from curso.xludw1ng.fastapi.jwtapi.dependencies.di import get_service
from curso.xludw1ng.fastapi.jwtapi.schemas.user_dto import UserDto
from curso.xludw1ng.fastapi.jwtapi.schemas.user_request import UserRequest
from curso.xludw1ng.fastapi.jwtapi.services.user_service import UserService

router = APIRouter()

@router.get('/', response_model=List[UserDto])
def list_users(service: UserService = Depends(get_service)):
    return service.find_all()

@router.get('/{user_id}', response_model=UserDto)
def get_user(user_id: int, service: UserService = Depends(get_service)):
    user = service.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@router.post('/', response_model=UserDto)
def create_user(user: UserRequest, service: UserService = Depends(get_service)):
    try:
        return service.create(user)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.json())
