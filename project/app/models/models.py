from sqlalchemy import Column, Boolean, FoerignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

from .database import Base


class TransactionType(Base):
    __tablename__ = "transaction_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128))
    description = Column(String(256))

    transactions = relationship("Transaction", back_populates="transaction_type")



class Transaction(Base):
    __tablename__ = "transcations"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    is_active = Column(Boolean, default=True)
    transaction_type_id = Column(Integer, FoerignKey("transaction_types.id"))

    transaction_type = relationship("TransactionType", back_populates="transactions")