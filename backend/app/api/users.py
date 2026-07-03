from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.user_service import create_user, get_users

router = APIRouter()

@router.post("/users")
def add_user(user: UserCreate):
    return create_user(user)

@router.get("/users")
def list_users():
    return get_users()