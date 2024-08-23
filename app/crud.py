from sqlalchemy.orm import Session
from . import models, schemas

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_account(db: Session, account: schemas.AccountCreate):
    db_account = models.Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.account_id == account_id).first()

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(**transaction.dict())
    account = db.query(models.Account).filter(models.Account.account_id == transaction.account_id).first()
    
    if transaction.transaction_type == 'Credit':
        account.balance += transaction.amount
    elif transaction.transaction_type == 'Debit':
        if account.balance >= transaction.amount:
            account.balance -= transaction.amount
        else:
            return None  # Insufficient funds
    
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
