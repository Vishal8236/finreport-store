from sqlalchemy import Column, DateTime, Integer, String, Float, Date
from app.db.base import Base
from datetime import datetime

class Employee(Base):
  __tablename__ = "employees"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True, index=True)
  phone_number = Column(String)
  address = Column(String)
  age = Column(Integer)
  salary = Column(Float, nullable=False)
  joining_date = Column(Date)
  left_date = Column(Date)
  leave = Column(Integer)
  added_by = Column(String)
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
  