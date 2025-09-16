# Chapter 1. 기본 서버 구성
------------------------------------------------------------------------------

bash> mkdir todos && cd todos
bash> python -m venv venv
bash> source venv/Scripts/activate
venv> deactivate

bash> python --version

# Python에 설치된 Package 목록 확인.
bash> python -m pip list 

# 현재 프로젝트에 설치된 모든 패키지 목록 저장.
bash> pip freeze > requirements.txt 
# txt에 있는 패키지를 모두 설치.
bash> pip install -r requirements.txt 

# fastAPI 설치 / 제거 
bash> pip install fastapi
bash> pip uninstall fastapi

# 환경 변수 Path에 경로 추가. (적용후 현재 Prompt창을 닫고, 새롭게 열어서 사용)
setx PATH "%PATH%;C:\Users\Username\myapp\scripts"

# 의존 API들은 venv에 설치 한다.
bash> source venv/Scripts/activate
venv> pip install fastapi uvicorn[standard]

# file:instance, port, --reload(파일 변경시 api 자동 재시작 적용)
# 웹서버 실행
venv> uvicorn api:app --port 8000 --reload 

# 웹서버 접속 테스트
other bash> curl http://localhost:8000/


# Chapter 2 : 라우팅
------------------------------------------------------------------------------
라우팅:
    클라이언트가 서버로 보내는 HTTP 요청을 처리하는 프로세스.
    HTTP요청이 지정한 라우트로 전송되면, 미리 정의된 로직이 해당 요청을 처리해서 반환한다.
HTTP 요청 메서드 : GET, POST, PUT, PATCH, DELETE


[2.1 APIRouter]
uvicorn은 하나의 엔트리 포인트만 실행할 수 있으므로, 라우트 관리가 필요하여, fastAPI에서는 APIRouter()를 제공한다.
APIRouter를 통해 라우팅과 로직을 독립적으로 구성할 수 있다.

todo.py 를 통해 Router 클래스 생성
uvicorn은 APIRouter() 인스턴스 바로 사용할수 없으므로, FastAPI 인스턴스에 APIRouter를 추가해준다.

# 웹서버 다시 실행 (열려 있다면, --reload에 의해 자동 갱신됨)
venv> uvicorn api:app --port 8000 --reload 

# 웹서버 라우트 확인
    -X GET
         HTTP 요청의 메서드를 지정합니다. 
    -H "accept: application/json"
        요청 **헤더(Header)**를 지정합니다.
        -H 헤더를 추가하는 옵션입니다.
        "accept: application/json" 클라이언트(여기서는 curl)가 서버로부터 JSON 형식의 응답을 받기를 원한다는 것을 서버에게 알리는 부분입니다.
# 아이템 추가
bash>curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\": 1, \"item\": \"My Item\"}"
# 아이템 리스트 확인
bash>curl -X GET http://127.0.0.1:8000/todo -H "accept: application/json"


[2.2 스키마 (pydanic 데이터검증 python library 사용)]
FastAPI에서는 정의된 데이터만 전송되도록 요청바디를 검증 할수 있다. 요청 데이터의 위험을 줄이는 중요한 기능이다.
FastAPI에서 모델은 데이터가  어떻게 전달되고 처리돼야 하는지 정의하는 구조화된 클래스를 말한다.
모델은 pydanic의 BaseModel를 파생하여 생성한다.

# pydanic 포멧에 맞게 Post를 보내서 내용을 저장하고, Get을 내용을 확인한다.
bash>
curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{"id": 1, "item": "Validation Models"}'
curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{"id": 1, "item": { "name": "apple", "status": "red"} }'
curl -X POST http://127.0.0.1:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d '{"id": 2, "item": { "name": "banana", "status": "yellow"} }'
curl -X GET http://127.0.0.1:8000/todo/1


# 요청 바디
 POST 와 UPDATE등 라우팅 메서드를 사용해 API로 전달되는 데이터
  - POST    : 새로운 데이터를 서버에 추가해준다
  - UPDATE  : 기존의 데이터를 변경해준다

# 인터렉티브 UI 
    # Swagger   : /docs
    # ReDoc     : /redoc
사용자가 입력해야 할 데이터 샘플을 설정하기 위해 모델 클래스 안에 Config 클래스를 정의 할수 있다.


# Chapter 3 : 응답 모델과 오류 처리
------------------------------------------------------------------------------