from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel


class TransactionBase(BaseModel):
    name: str
    description: Optional[str] = None


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    is_active: bool
    created_at: datetime
    transaction_type_id: int

    class Config:
        orm_mode = True




class TransactionTypeBase(BaseModel):
    name: str
    description: Optional[str] = None


class TransactionTypeCreate(TransactionTypeBase):
    pass


class TransactionType(TransactionTypeBase):
    id: int
    transactions: List[Transaction] = []

    class Config:
        orm_mode = True