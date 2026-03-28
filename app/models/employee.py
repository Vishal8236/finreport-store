from sqlalchemy import Column, DateTime, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
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
  store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
  store = relationship("Store", back_populates="employees")
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
  