from sqlalchemy.orm import Session
from app.models.store import Store
from app.core.auth import get_password_hash, verify_password

def create_store(db: Session, store_data):
  hashed_password = get_password_hash(store_data.password)
  db_store = Store(
    store_name=store_data.store_name,
    email=store_data.email,
    password=hashed_password
  )
  db.add(db_store)
  db.commit()
  db.refresh(db_store)
  return db_store

def authenticate_store(db: Session, email: str, password: str):
  store = db.query(Store).filter(Store.email == email).first()
  if not store:
    return False
  if not verify_password(password, store.password):
    return False
  return store