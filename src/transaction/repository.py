from sqlalchemy import UUID
from sqlalchemy.orm import Session
from . import models, schemas

class TransactionRepository:
    def get_transaction_by_transaction_id(db: Session, transaction_id: UUID):
        transaction = db.query(models.Transaction).filter(models.Transaction.transaction_id == transaction_id)
        return transaction
    
    def get_transactions(db: Session, offset: int = 0, limit: int = 100):
        transactions = db.query(models.Transaction).offset(offset).limit(limit).all()
        return transactions
    
    def create_transaction(db: Session, transaction: schemas.TransactionCreate):
        db_transaction = models.Transaction(
            amount = transaction.amount,
            description = transaction.description,
            category = transaction.category,
            date = transaction.date,
            account_id = transaction.account_id
        )
        
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction

        