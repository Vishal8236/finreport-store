from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Store(Base):
  __tablename__ = "stores"

  id = Column(Integer, primary_key=True, index=True)
  store_name = Column(String, nullable=False)
  email = Column(String, unique=True, index=True)
  password = Column(String, nullable=False)
  employees = relationship("Employee", back_populates="store")
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)