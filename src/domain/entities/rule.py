from sqlalchemy import Column, Integer, String

from src.domain.db.config import Base


class Rule(Base):
    __tablename__ = "rules"

    rule_id = Column(Integer, primary_key=True, autoincrement=True)
    rule_key = Column(String(length=255), nullable=False)
    recommended_product = Column(String(length=255), nullable=False)

    def __init__(self, rule_key, recomended_product):
        self.rule_key = rule_key
        self.recommended_product = recomended_product
