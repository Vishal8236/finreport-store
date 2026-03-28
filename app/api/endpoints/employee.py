from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.services.employee_service import create_employee, get_all_employees
from app.core.dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
  return get_all_employees(db)

@router.post("/", response_model=EmployeeResponse)
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
  return create_employee(db, employee)