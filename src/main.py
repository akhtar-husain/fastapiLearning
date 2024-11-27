from fastapi import APIRouter
from src.pathParams import router as pathRouter
from src.queryParams import router as queryRouter

router = APIRouter()

router.include_router(pathRouter)
router.include_router(queryRouter)
