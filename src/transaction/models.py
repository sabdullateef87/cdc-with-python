from pydantic import BaseModel
from typing import Optional
import uuid

from sqlalchemy import UUID, Column, DateTime, Double, Float, Integer, String
from config import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    
    transaction_id = Column(String, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    amount = Column(Float)
    description = Column(String, index=True)
    category = Column(String, index=True)
    date = Column(DateTime)
    account_id = Column(String)
