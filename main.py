from fastapi import FastAPI
from routers import task, user

app = FastAPI()
# cd app
# python -m uvicorn main:app

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# объединить все маршруты в одно приложение.
app.include_router(user.router)
app.include_router(task.router)