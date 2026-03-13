import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')
    JWT_TIME_EXP: int = int(os.getenv('JWT_TIME_EXP'))
    BASE_URL: str = os.getenv('BASE_URL')

settings = Settings()
