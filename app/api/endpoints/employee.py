from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services.employee_service import create_employee, get_all_employees, update_employee, delete_employee
from app.core.dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
  return get_all_employees(db)

@router.post("/", response_model=EmployeeResponse)
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
  return create_employee(db, employee)

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee_endpoint(employee_id: int, employee_update: EmployeeUpdate, db: Session = Depends(get_db)):
  updated_employee = update_employee(db, employee_id, employee_update)
  if not updated_employee:
    raise HTTPException(status_code=404, detail="Employee not found")
  return updated_employee

@router.delete("/{employee_id}")
def delete_employee_endpoint(employee_id: int, db: Session = Depends(get_db)):
  deleted = delete_employee(db, employee_id)
  if not deleted:
    raise HTTPException(status_code=404, detail="Employee not found")
  return {"message": "Employee deleted successfully"}