from sqlmodel import SQLModel, Session, create_engine
from models.events import Event


database_filename = "planner.db"
database_connection = f"sqlite:///{database_filename}"
connect_args = {"check_same_thread": False} 
engine_url = create_engine(database_connection, echo=True, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session

