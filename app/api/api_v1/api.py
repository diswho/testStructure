from fastapi import APIRouter

from app.api.api_v1.endpoints import attendance

api_router = APIRouter()
api_router.include_router(
    attendance.router, prefix="/attendance", tags=["Attendance"])
