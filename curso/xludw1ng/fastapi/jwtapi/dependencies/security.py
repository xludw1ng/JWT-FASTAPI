from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from curso.xludw1ng.fastapi.jwtapi.config.settings import settings
from curso.xludw1ng.fastapi.jwtapi.dependencies.di import get_repository
from curso.xludw1ng.fastapi.jwtapi.entities.users import User
from curso.xludw1ng.fastapi.jwtapi.repositories.user_repository import UserRepository

#LEE EL HEADER DE CADA PETICION
oath2_scheme = OAuth2PasswordBearer(tokenUrl="/oauth/token/form")

def get_current_user(repo: UserRepository = Depends(get_repository), token: str = Depends(oath2_scheme)) -> User:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        user_id = int(payload.get("sub"))
    except(JWTError, TypeError, ValueError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

    user = repo.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

    return user