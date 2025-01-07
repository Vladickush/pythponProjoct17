from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()
'''Неочевидный момент:

Если ваш файл main.py находится внутри папки app, запуск сервера потребует указания пути к этому файлу. В FastAPI используется uvicorn, который вы можете запустить из командной строки:

uvicorn app.main:app --reload

app.main: Это путь к файлу main.py, где app — имя папки, а main — имя файла (без расширения .py).
:app: Это ссылка на объект FastAPI, созданный внутри файла main.py (обычно переменная app).
--reload: Эта опция автоматически перезапускает сервер при изменении кода (удобно для разработки).

Есть способ перейти в папку app и запустить задачу из неё.  
# cd app
# python -m uvicorn main:app'''



@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# объединить все маршруты в одно приложение.
app.include_router(user.router)
app.include_router(task.router)