"""main.py
Python FastAPI Auth0 integration example
"""
from typing import Optional
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header, Response, Depends, status
from fastapi.security import HTTPBearer
from auth import VerifyToken

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

origins = ["*"]

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


@app.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be "
                "authenticated to see this.")
    }
    return result


@app.get("/api/header")
def private(token: str = Depends(token_auth_scheme)):
    """A valid access token is required to access this route"""

    result = token.credentials

    return result


@app.get("/api/private")
def private(response: Response, token: str = Depends(token_auth_scheme)):
    """A valid access token is required to access this route"""

    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    return result
