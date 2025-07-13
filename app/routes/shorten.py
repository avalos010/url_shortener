from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.database import insert_url
import uuid

router = APIRouter()
@router.post("/shorten")
async def shorten_url(request: Request):
    data = await request.json()
    original_url = data["original_url"]
    shortened_url = str(uuid.uuid4())[:6]
    insert_url(original_url, shortened_url)
    return {"shortened_url": shortened_url}
