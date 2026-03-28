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

def update_employee(db: Session, employee_id: int, employee_update):
  employee = db.query(Employee).filter(Employee.id == employee_id).first()
  if not employee:
    return None
  
  update_data = employee_update.dict(exclude_unset=True)
  for field, value in update_data.items():
    if value is not None:
      setattr(employee, field, value)
  
  db.commit()
  db.refresh(employee)
  return employee

def delete_employee(db: Session, employee_id: int):
  employee = db.query(Employee).filter(Employee.id == employee_id).first()
  if not employee:
    return False
  
  db.delete(employee)
  db.commit()
  return True