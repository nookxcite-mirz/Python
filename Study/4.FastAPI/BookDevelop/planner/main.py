from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from database.connection import engine, Base

import uvicorn

app = FastAPI()

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# uvicorn.run() 을 사용하여 API 실행
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


