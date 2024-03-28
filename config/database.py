import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def build_database_connection_string():
    user = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_USERNAME')
    db = os.environ.get('DB_USERNAME')
    host = os.environ.get('DB_USERNAME')
    port = os.environ.get('DB_USERNAME')
    return f'postgresql://{user}:{password}@{host}:{port}/{db}'
    
SQLALCHEMY_DATABASE_URL = build_database_connection_string()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
