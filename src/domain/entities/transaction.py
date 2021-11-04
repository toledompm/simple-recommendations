from sqlalchemy import Column, Integer

from src.domain.db.config import Base


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
