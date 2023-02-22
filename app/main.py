"""main.py
Python FastAPI Auth0 integration example
"""
from typing import Optional
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header
from fastapi.security import HTTPBearer

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

origins = ["*"]

# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()
app = FastAPI(middleware=middleware)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
async def post_root():
    return {"message": "Post request success"}


@app.get("/hello")
async def root():
    return {"message": "Hello FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/headers")
async def read_headers(user_agent: str | None = Header(None)):
    return {"User-Agent": user_agent}
