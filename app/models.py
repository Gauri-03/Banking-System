from sqlalchemy import Column, Integer, String, Date, ForeignKey, DECIMAL, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Customer(Base):
    __tablename__ = "Customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    address = Column(String(255))
    date_of_birth = Column(Date)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

    accounts = relationship("Account", back_populates="owner")


class Account(Base):
    __tablename__ = "Accounts"

    account_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("Customers.customer_id"))
    account_number = Column(String(20), unique=True)
    account_type = Column(Enum('Savings', 'Checking'))
    balance = Column(DECIMAL(10, 2), default=0.00)
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

    owner = relationship("Customer", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")


class Transaction(Base):
    __tablename__ = "Transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("Accounts.account_id"))
    amount = Column(DECIMAL(10, 2))
    transaction_type = Column(Enum('Credit', 'Debit'))
    transaction_date = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")

    account = relationship("Account", back_populates="transactions")
