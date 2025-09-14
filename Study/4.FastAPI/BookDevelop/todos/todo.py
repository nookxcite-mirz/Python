from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []

# todo 처리를 위해 두개의 라우트를 추가함.

@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos" : todo_list
    }