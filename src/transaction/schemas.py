from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount : float
    account_id : str
    
    
    
class TransactionCreate(BaseModel):
    amount: float
    description : str
    category :  str
    date : str
    account_id : str
    
    class Config:
        orm_mode = True
    
