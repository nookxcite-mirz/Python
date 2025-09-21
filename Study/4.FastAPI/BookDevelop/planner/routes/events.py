from fastapi import APIRouter, HTTPException, Request, status, Depends
from database.connection import get_session
from models.events import Event, EventUpdate
from sqlmodel import select
from typing import List

event_router = APIRouter(
    tags=["Events"],
)

events = []

event_counter = 1

@event_router.get("/", response_model=List[Event])
async def get_all_events(session=Depends(get_session)) -> List[Event]:
    """모든 이벤트 조회"""
    statement = select(Event)
    events = session.exec(statement).all()
    return events

@event_router.get("/{id}", response_model=Event)
async def get_event(id: int, session=Depends(get_session)) -> Event:
    """특정 이벤트 조회"""
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")


@event_router.post("/new")
async def create_event(new_event:Event, session=Depends(get_session)) -> dict:
    """새 이벤트 생성"""
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {"message": "Event created successfully", "event_id": new_event.id}

@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    """이벤트 수정"""
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.commit()
        session.refresh(event)
        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    

@event_router.delete("/delete/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    """이벤트 삭제"""
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        return {"message": "Event deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Event not found"
    )
