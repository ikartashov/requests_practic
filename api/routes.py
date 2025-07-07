from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import HTMLResponse
from app.services import get_user,create_user, update_user, delete_user
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="API пользователей",
              description='Мини проект "Пользователи"')
class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None

class UserCreate(BaseModel):
    name: str
    username: str
    email: str


@app.get('/')
def root():
    html_content = ('<h1>Добро пожаловать в API пользователей! Для работы с приложением зайдите в документацию Swagger.</h1>')
    return HTMLResponse(content=html_content)

@app.get('/users/{user_id}')
def api_get_user(user_id: int):
    user = get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")

@app.post('/users')
def app_create_user(user:UserCreate = Body(...)):
    created = create_user(user.model_dump(exclude_unset=False))
    if created:
        return created
    raise HTTPException(status_code=400, detail="Ошибка при создании пользователя")

@app.patch('/users/{user_id}')
def app_update_user(user_id: int, data: UserUpdate = Body(...)):
    updated = update_user(user_id, data.model_dump(exclude_unset=True))
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Пользователь не найден или ошибка обновления")

@app.delete('/users/{user_id}')
def app_delete_user(user_id: int):
    deleted = delete_user(user_id)
    if deleted:
        return deleted
    raise HTTPException(status_code=404, detail="Пользователь не найден")



