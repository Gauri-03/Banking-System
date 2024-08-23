from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    date_of_birth: date

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    customer_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    account_number: str
    account_type: str
    balance: Optional[float] = 0.00

class AccountCreate(AccountBase):
    customer_id: int

class Account(AccountBase):
    account_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    amount: float
    transaction_type: str

class TransactionCreate(TransactionBase):
    account_id: int

class Transaction(TransactionBase):
    transaction_id: int
    transaction_date: datetime

    class Config:
        orm_mode = True
