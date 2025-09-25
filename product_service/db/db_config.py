from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://product:product%401234@127.0.0.7:5002/product_service_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def db_connection():
     db = SessionLocal()
     try:
          yield db
          
     finally:
          db.close()