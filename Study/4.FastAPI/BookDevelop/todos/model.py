from pydantic import BaseModel

class Item(BaseModel):
    name: str
    status: str

class TodoItem(BaseModel):
    item: str
    class Config:
        schema_extra = {
            "example": {
                "item": "Item Name"                    
            }
        }



class Todo(BaseModel):
    id: int
    item: Item

    # Swagger의 문서에 표시된다. (데이터로 기능되지는 않는다.)
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": {
                    "name": "apple",
                    "status": "red"
                }
            }
        }