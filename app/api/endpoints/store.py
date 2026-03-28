from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from app.schemas.store import StoreCreate, StoreLogin, StoreResponse, Token
from app.services.store_service import create_store, authenticate_store
from app.core.auth import create_access_token, authenticate_store as auth_store, ACCESS_TOKEN_EXPIRE_MINUTES
from app.core.dependencies import get_db
from app.models.store import Store

router = APIRouter()

@router.post("/register", response_model=StoreResponse)
def register_store(store: StoreCreate, db: Session = Depends(get_db)):
  db_store = db.query(Store).filter(Store.email == store.email).first()
  if db_store:
    raise HTTPException(status_code=400, detail="Email already registered")
  return create_store(db, store)

@router.post("/login", response_model=Token)
def login_store(store_credentials: StoreLogin, db: Session = Depends(get_db)):
  store = auth_store(db, store_credentials.email, store_credentials.password)
  if not store:
    raise HTTPException(
      status_code=401,
      detail="Incorrect email or password",
      headers={"WWW-Authenticate": "Bearer"},
    )
  access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = create_access_token(
    data={"sub": str(store.id)}, expires_delta=access_token_expires
  )
  return {"access_token": access_token, "token_type": "bearer"}