from random import random
from enum import Enum
from fastapi import APIRouter

router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.get("/users/me")
async def getCurrentUser():
    """
    Get current user
    """
    return {"userId": 1, "name": "Akhtar Husain"}


@router.get("/users/{username}")
async def getUserDetail(username: str):
    """
    Get user by username
    """
    return {"userId": int(random() * 100), "name": username.title()}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@router.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    Let's say you have a path operation with a path /files/{file_path}.\n
    But you need file_path itself to contain a path, like home/johndoe/myfile.txt.\n
    So, the URL for that file would be something like: /files/home/johndoe/myfile.txt
    """
    return {"file_path": file_path}
