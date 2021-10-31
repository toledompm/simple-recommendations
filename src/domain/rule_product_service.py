from src.domain.entities.rule_product import RuleProduct
from src.domain.repositories.rule_product_repository import (
    get_rule_ids_by_product_ids,
    save,
    get_products_by_rule_id,
)


def create_rule_product(rule, product):
    rule_product = RuleProduct(rule_id=rule.rule_id, product_id=product.product_id)
    save(rule_product)


def get_rule_ids(product_ids):
    return get_rule_ids_by_product_ids(product_ids)


def get_products(rule_id):
    return get_products_by_rule_id(rule_id)
