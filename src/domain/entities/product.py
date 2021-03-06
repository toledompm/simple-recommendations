from sqlalchemy import Column, Integer, String

from src.domain.db.config import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(length=255), nullable=False)
    product_slug = Column(String(length=255), nullable=False)

    def __init__(self, product_name, product_slug):
        self.product_name = product_name
        self.product_slug = product_slug
