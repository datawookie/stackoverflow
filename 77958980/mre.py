from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import db

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.middleware("http")
async def add_process_time_header(request, call_next):
    if db.is_closed():
        db.connect()

    response = await call_next(request)

    return response

@app.get("/")
async def root():
    return {"message": f"Hello World!"}
