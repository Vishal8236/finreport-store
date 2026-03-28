from fastapi import APIRouter
from app.api.endpoints import employee

api_router = APIRouter()

api_router.include_router(employee.router, prefix="/employee", tags=["Employee"])