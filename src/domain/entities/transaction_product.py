from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey

from src.domain.db.config import Base


class TransactionProduct(Base):
    __tablename__ = "transaction_products"

    transaction_product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    transaction_id = Column(Integer, ForeignKey("transactions.transaction_id"), nullable=False)

    def __init__(self, transaction_id, product_id):
        self.transaction_id = transaction_id
        self.product_id = product_id
