from pydantic import BaseModel
from datetime import datetime

class StoreCreate(BaseModel):
  store_name: str
  email: str
  password: str

class StoreLogin(BaseModel):
  email: str
  password: str

class StoreResponse(BaseModel):
  id: int
  store_name: str
  email: str
  created_at: datetime | None = None
  updated_at: datetime | None = None

  class Config:
    from_attributes = True

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  store_id: int | None = None