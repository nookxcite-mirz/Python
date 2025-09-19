from fastapi import FastAPI

# todo.py 파일에서 Router 클래스 임포트 (Chapter 2)
from todo import todo_router

app = FastAPI()

# -> dict는 파이썬의 타입 힌트(Type Hint) 문법으로, 함수가 반환하는 값의 타입(dict)을 명시적으로 알려주는 역할을 합니다.
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello, World!"}

    
# todo_router 클래스를 추가함.
app.include_router(todo_router)

# venv> uvicorn api:app --port 8000 --reload
"""
curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":1, \"item\": \"This todo will be retrieved without exposing the ID\"}"
curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":2, \"item\": \"This todo will be retrieved without exposing the ID\"}"
curl -X GET http://127.0.0.1:8000/todo -H "accept: application/json"
"""
# 8000번 포트에서 서버 실행.
