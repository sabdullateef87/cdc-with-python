from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount : float
    account_id : str
    
    
