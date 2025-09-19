from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item


class TodoItem(BaseModel):
    id: int
    item: str
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Read the next chapter of the book"                    
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
