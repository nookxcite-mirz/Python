from fastapi import APIRouter, Path, HTTPException, status, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems, Item 


todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="templates/")

# todo 처리를 위해 두개의 라우트를 추가함. 입력 주소를 통해 데이터를 전달받아 처리한다.

@todo_router.post("/todo", status_code=status.HTTP_201_CREATED)
#async def add_todo(todo: dict) -> dict:
async def add_todo(todo: TodoItem) -> dict:         # 입력받을 타입을 TodoItem으로 지정
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

# 출력 모델을 TodoItems로 지정
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {
        "todos" : todo_list
    }

# 경로 매개 변수를 통해 지정한 ID와 일치하는 todo 데이터를 반환 한다.
# - Path 클래스를 사용해 경로 매개변수와 다른 인수를 구분하며, Swagger의 문서에 표시된다.
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., description="the ID of the todo retrieve.")) -> dict:    
    for todo in todo_list:
        if todo.id == todo_id:
            return { "todo" : todo }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
        

# 쿼리 매개 변수 
# - URL에서 ?뒤에 오면 선택사항으로, 제공된 커리를 기반으로 특정값 반환 및 필터링 할때 사용한다.
#async def query_route(query: str = Query(None)):
#    return query


# 업데이트용 라우트 - PUT 요청을 통해 데이터를 업데이트 한다.
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., description="the ID of the todo to be update.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return { "message": "Todo updated successfully" }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

# bash> curl -X PUT http://127.0.0.1:8000/todo/1 -H "accept: application/json" -H "Content-Type: application/json" -d '{"item": "Updated Item"}'

# 삭제용 라우트 - DELETE 요청을 통해 데이터를 삭제 한다.
@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return { "message": "Todo deleted successfully" }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied ID doesn't exist")
    
# bash> curl -X DELETE http://127.0.0.1:8000/todo/1 -H "accept: application/json"

# 모든 데이터 삭제용 라우트 - DELETE 요청을 통해 모든 데이터를 삭제 한다.
@todo_router.delete("/todo/all")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return { "message": "All todos deleted successfully" }

# bash> curl -X DELETE http://127.0.0.1:8000/todo/all -H "accept: application/json" 



# templating Post/Get 라우트
#-----------------------------------------------------------------------------------
@todo_router.post("/todo_template")
async def add_todo_template(
    request: Request, 
    item: str = Form(...)
):
    todo_id = len(todo_list) + 1
    todo = TodoItem(id=todo_id, item=item)
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html",
    {
        "request": request,
        "todos":todo_list
        })

@todo_router.get("/todo_template")
async def retrieve_todos_template(request: Request):
    return templates.TemplateResponse("todo.html",
    {
        "request": request,
        "todos" : todo_list
    })

@todo_router.get("/todo_template/{todo_id}")
async def get_single_todo_template(request: Request, todo_id: int = Path(..., description="the ID of the todo retrieve.")):    
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse("todo.html",
            {
                "request": request,
                "todo" : todo
            })
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
