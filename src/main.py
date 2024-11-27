from fastapi import APIRouter
from src.pathParams import router as pathRouter
from src.queryParams import router as queryRouter
from src.requestBody import router as requestRouter

router = APIRouter()

router.include_router(pathRouter, prefix="/pr")
router.include_router(queryRouter, prefix="/qr")
router.include_router(requestRouter, prefix="/rr")
