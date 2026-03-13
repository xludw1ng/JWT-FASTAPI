from fastapi import FastAPI

from curso.xludw1ng.fastapi.jwtapi.config.db import engine, Base
import curso.xludw1ng.fastapi.jwtapi.entities.users

app = FastAPI()

Base.metadata.create_all(bind = engine)


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None):
    return {'item_id': item_id, 'q': q}
