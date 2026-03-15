from datetime import datetime, timedelta, timezone

from jose import jwt

from curso.xludw1ng.fastapi.jwtapi.config.settings import settings


def create_access_token(subject: str):

    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_TIME_EXP)
    payload = {'sub': subject, 'exp': expire}
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token