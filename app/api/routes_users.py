from fastapi import APIRouter
from app.services.user_service import get_all_users

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def list_users():
    users = get_all_users()
    return {"users": users}
