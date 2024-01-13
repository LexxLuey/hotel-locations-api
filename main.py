from typing import Optional
from fastapi import FastAPI, Request

# from router import user
from router import hotel
from router import chain
from db.database import engine
from db import models
from exceptions import StoryException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# app.include_router(user.router)
app.include_router(chain.router)
app.include_router(hotel.router)


@app.get("/hello")
def index():
    return {"message": "Hello world!"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.name})


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#   return PlainTextResponse(str(exc), status_code=400)

models.Base.metadata.create_all(engine)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
