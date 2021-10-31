from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from src.domain.db.config import Base


class RuleProduct(Base):
    __tablename__ = "rule_products"

    rule_product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    rule_id = Column(Integer, ForeignKey("rules.rule_id"), nullable=False)

    product = relationship("Product", cascade="all,delete", foreign_keys=[product_id])
    rule = relationship("Rule", cascade="all,delete", foreign_keys=[rule_id])

    def __init__(self, rule_id, product_id):
        self.rule_id = rule_id
        self.product_id = product_id
