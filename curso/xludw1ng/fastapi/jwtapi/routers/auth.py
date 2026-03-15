from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from curso.xludw1ng.fastapi.jwtapi.dependencies.di import get_repository
from curso.xludw1ng.fastapi.jwtapi.repositories.user_repository import UserRepository
from curso.xludw1ng.fastapi.jwtapi.schemas.auth import TokenDTO, LoginRequest
from curso.xludw1ng.fastapi.jwtapi.security.jwt import create_access_token
from curso.xludw1ng.fastapi.jwtapi.security.passwords import verify_password
from curso.xludw1ng.fastapi.jwtapi.services.user_service import UserService

router = APIRouter()

#con postman/imnsomina/bruno necesita -json
@router.post("/token", response_model=TokenDTO)
def login(data: LoginRequest, repository: UserRepository = Depends(get_repository)):
    user = repository.find_by_email(data.email)
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

    token = create_access_token(subject=str(user.id))
    return {'access_token': token}

#con swaggerr necesta data-form
@router.post("/token/form", response_model=TokenDTO)
def login_form(data_form: OAuth2PasswordRequestForm = Depends(), repository: UserRepository = Depends(get_repository)):
    return login(LoginRequest.model_validate({
        "email": data_form.username,
        "password": data_form.password,
    }), repository)
