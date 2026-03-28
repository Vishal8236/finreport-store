from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.models.employee import Employee
from app.api.router import api_router

# import models (IMPORTANT)
from app.models import ledger

app = FastAPI()
app.include_router(api_router, prefix="/api")

# create tables
Base.metadata.create_all(bind=engine)