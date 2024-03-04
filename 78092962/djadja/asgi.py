from fastapi import FastAPI

application = FastAPI()


@application.get("/")
async def read_root():
    return {"Hello": "World"}
