from sqlalchemy.orm import Session
from app.models.employee import Employee

def get_all_employees(db: Session):
  return db.query(Employee).all()

def create_employee(db: Session, employee_data):
  employee = Employee(**employee_data.dict())
  db.add(employee)
  db.commit()
  db.refresh(employee)
  return employee