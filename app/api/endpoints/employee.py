from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services.employee_service import create_employee, get_employees_by_store, update_employee, delete_employee
from app.core.dependencies import get_db
from app.core.auth import get_current_store
from app.models.store import Store

router = APIRouter()

@router.get("/", response_model=List[EmployeeResponse])
def get_employees(current_store: Store = Depends(get_current_store), db: Session = Depends(get_db)):
  return get_employees_by_store(db, current_store.id)

@router.post("/", response_model=EmployeeResponse)
def add_employee(employee: EmployeeCreate, current_store: Store = Depends(get_current_store), db: Session = Depends(get_db)):
  return create_employee(db, employee, current_store.id)

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee_endpoint(employee_id: int, employee_update: EmployeeUpdate, current_store: Store = Depends(get_current_store), db: Session = Depends(get_db)):
  updated_employee = update_employee(db, employee_id, employee_update, current_store.id)
  if not updated_employee:
    raise HTTPException(status_code=404, detail="Employee not found or access denied")
  return updated_employee

@router.delete("/{employee_id}")
def delete_employee_endpoint(employee_id: int, current_store: Store = Depends(get_current_store), db: Session = Depends(get_db)):
  deleted = delete_employee(db, employee_id, current_store.id)
  if not deleted:
    raise HTTPException(status_code=404, detail="Employee not found or access denied")
  return {"message": "Employee deleted successfully"}