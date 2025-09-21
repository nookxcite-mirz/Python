from pydantic import BaseModel
from sqlmodel import SQLModel, Field, JSON, Column
from typing import List, Optional

"""
class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "Event 1 description",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
"""

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "Event 1 description",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None       
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "Event 1 description",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }