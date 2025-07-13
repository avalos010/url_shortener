from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.database import get_url

router = APIRouter()

@router.get("/redirect/{shortened_url}")
def redirect_url(shortened_url: str):
    original_url = get_url(shortened_url)
    if original_url:
        return {"original_url": original_url}
    else:
        return {"error": "URL not found"}