import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api.v1.api import router

app = FastAPI()

origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
