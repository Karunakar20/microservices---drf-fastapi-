# main.py
from datetime import timedelta
from fastapi import FastAPI, Depends, APIRouter
from auth import AuthService

app = FastAPI()
router = APIRouter()
auth_service = AuthService()


class Routes:
     """All FastAPI endpoints."""

     @staticmethod
     @router.get("/")
     async def public():
          return {"message": "Anyone can see this message"}

     @staticmethod
     @router.get("/test")
     async def test(_: dict = Depends(auth_service.test)):
          # If token is valid, just return a message
          return {"message": "JWT validated successfully!"}


app.include_router(router)
