from fastapi import FastAPI
from src.main import router

app = FastAPI(title="FastAPI Learning")


@app.get("/")
async def root():
    return {"message": "Hello World!"}


app.include_router(router)
