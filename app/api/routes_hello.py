from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["Hello"])

@router.get("/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! This is a modular FastAPI app."}
