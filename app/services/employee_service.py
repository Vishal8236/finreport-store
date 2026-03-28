from sqlalchemy.orm import Session, joinedload
from app.models.employee import Employee

def get_employees_by_store(db: Session, store_id: int):
  return db.query(Employee).options(joinedload(Employee.store)).filter(Employee.store_id == store_id).all()

def create_employee(db: Session, employee_data, store_id: int):
  employee_dict = employee_data.dict()
  employee_dict['store_id'] = store_id
  employee = Employee(**employee_dict)
  db.add(employee)
  db.commit()
  db.refresh(employee)
  return employee

def update_employee(db: Session, employee_id: int, employee_update, store_id: int):
  employee = db.query(Employee).filter(Employee.id == employee_id, Employee.store_id == store_id).first()
  if not employee:
    return None
  
  update_data = employee_update.dict(exclude_unset=True)
  for field, value in update_data.items():
    if value is not None:
      setattr(employee, field, value)
  
  db.commit()
  db.refresh(employee)
  return employee

def delete_employee(db: Session, employee_id: int, store_id: int):
  employee = db.query(Employee).filter(Employee.id == employee_id, Employee.store_id == store_id).first()
  if not employee:
    return False
  
  db.delete(employee)
  db.commit()
  return True