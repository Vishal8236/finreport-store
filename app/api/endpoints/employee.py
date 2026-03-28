from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.services.employee_service import create_employee
from app.core.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=EmployeeResponse)
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
  return create_employee(db, employee)