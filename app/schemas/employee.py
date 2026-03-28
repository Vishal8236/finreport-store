from pydantic import BaseModel
from datetime import date, datetime

class EmployeeCreate(BaseModel):
  name: str
  email: str
  phone_number: str | None = None
  age: int | None = None
  salary: float
  joining_date: date | None = None
  left_date: date | None = None
  leave: int | None = None
  added_by: str | None = None

class EmployeeResponse(BaseModel):
  id: int
  name: str
  email: str
  phone_number: str | None = None
  age: int | None = None
  salary: float
  joining_date: date | None = None
  left_date: date | None = None
  leave: int | None = None
  added_by: str | None = None
  created_at: datetime | None = None
  updated_at: datetime | None = None

  class Config:
    from_attributes = True
        