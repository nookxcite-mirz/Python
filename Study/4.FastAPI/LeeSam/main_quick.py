
"""
Union 타입을 사용하여 여러 타입을 허용
"""
from typing import Union
from pydantic import BaseModel

"""
FastAPI 프레임워크 임포트
"""
from fastapi import FastAPI

"""
FastAPI 인스턴스 생성
서버 실행시 main이 되는 인스턴스 이름이로 main:app 로 실행한다.
"""
app = FastAPI()


"""
Item 모델 정의
- name: 상품명 (문자열)
- price: 가격 (실수형)
- is_offer: 할인 여부 (bool 또는 None, 기본값 None)
"""
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


"""
루트 경로에 GET 요청이 오면 아래 함수 실행
간단한 JSON 응답 반환
"""
@app.get("/")
def read_root():
    return {"Hello": "World"}

"""
/items/{item_id} 경로에 GET 요청이 오면 아래 함수 실행
item_id와 q 값을 JSON으로 반환
"""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

"""
PUT 요청을 통해 /items/{item_id} 경로로 들어온 요청을 처리
- item_id: URL 경로에서 전달받은 아이템의 ID (정수형)
- item: 요청 본문에서 전달받은 Item 모델 데이터 (name, price, is_offer)
- 반환값: 수정된 아이템의 이름과 ID를 JSON 형태로 반환
"""
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# uvicorn main:app --reload / Ctlr+C(종료)
