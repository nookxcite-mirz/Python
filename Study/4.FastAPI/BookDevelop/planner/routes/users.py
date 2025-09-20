from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn
from utils import hash_password, verify_password

user_router = APIRouter(
    tags=["User"],
)

users = {}

@user_router.post("/signup")
async def sign_new_user(user_data: User) -> dict:
    """새 사용자 등록"""
    if user_data.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with supplied username exists")
    
    # 비밀번호 해싱
    hashed_password = hash_password(user_data.password)
    user_data.password = hashed_password
    
    users[user_data.email] = user_data
    return { "message": "User successfully registered" }

@user_router.post("/signin", status_code=status.HTTP_200_OK)
async def sign_user_in(user_data: UserSignIn) -> dict:
    """사용자 로그인"""
    if user_data.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User with supplied username does not exist")
    
    # 해싱된 비밀번호와 비교
    if not verify_password(user_data.password, users[user_data.email].password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
    return { "message": "User signed in successfully" }

