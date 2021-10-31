from sqlalchemy import true
from src.domain.db.config import session
from src.domain.entities.product import Product
from src.domain.entities.rule_product import RuleProduct
from src.infra.cache import custom_lru_cache


def save(rule_product: RuleProduct):
    session.add(rule_product)
    session.commit()
    get_products_by_rule_id.cache_remove(rule_product.rule_id)
    get_rule_ids_by_product_ids.clear_cache()
    return rule_product


def get_rule_ids_by_product_ids(product_ids):
    rule_products = (
        session.query(RuleProduct).filter(RuleProduct.product_id.in_(product_ids)).all()
    )
    return list(set([rule_product.rule_id for rule_product in rule_products]))


@custom_lru_cache
def get_products_by_rule_id(rule_id):
    return session.query(RuleProduct).filter(RuleProduct.rule_id == rule_id).all()
