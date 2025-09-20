from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 데이터베이스 URL 설정 (환경변수에서 가져오거나 기본값 사용)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./planner.db")

# SQLAlchemy 엔진 생성
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성 (모델들이 상속받을 클래스)
Base = declarative_base()

def get_db():
    """데이터베이스 세션을 가져오는 의존성 함수"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
