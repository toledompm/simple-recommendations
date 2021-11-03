from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from src.domain.db.config import Base


class Rule(Base):
    __tablename__ = "rules"

    rule_id = Column(Integer, primary_key=True, autoincrement=True)
    recommended_product_id = Column(
        Integer, ForeignKey("products.product_id"), nullable=False
    )

    recommended_product = relationship("Product", foreign_keys=[recommended_product_id])

    def __init__(self, recommended_product):
        self.recommended_product = recommended_product
