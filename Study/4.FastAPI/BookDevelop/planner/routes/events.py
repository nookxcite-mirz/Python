from fastapi import APIRouter, HTTPException, status, Body
from models.events import Event
from typing import List

event_router = APIRouter(
    tags=["Events"],
)


events = []

event_counter = 1

@event_router.get("/", response_model=List[Event])
async def get_all_events() -> List[Event]:
    """모든 이벤트 조회"""
    return events

@event_router.get("/{id}", response_model=Event)
async def get_event(id: int) -> Event:
    """특정 이벤트 조회"""
    for event in events:
        if event.id == id:
            return event
    raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Event not found" )

@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    """새 이벤트 생성"""
    global event_counter
    body.id = event_counter
    events.append(body)
    event_counter += 1
    return {"message": "Event created successfully", "event_id": body.id}

@event_router.put("/{id}")
async def update_event(id: int, body: Event = Body(...)) -> dict:
    """이벤트 수정"""
    for i, event in enumerate(events):
        if event.id == id:
            body.id = id
            events[i] = body
            return {"message": "Event updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Event not found"
    )

@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    """이벤트 삭제"""
    for i, event in enumerate(events):
        if event.id == id:
            del events[i]
            return {"message": "Event deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Event not found"
    )
