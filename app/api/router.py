from fastapi import APIRouter
from app.api.endpoints import employee, store

api_router = APIRouter()

api_router.include_router(store.router, prefix="/store", tags=["Store"])
api_router.include_router(employee.router, prefix="/employee", tags=["Employee"])