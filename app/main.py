from fastapi import FastAPI
from app.routes.redirect import router as redirect_url
from app.routes.shorten import router as shorten_url

app = FastAPI()

app.include_router(redirect_url)
app.include_router(shorten_url)