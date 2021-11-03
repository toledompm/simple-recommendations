from src.domain.entities.rule import Rule
from src.domain.product_service import find_or_create_product
from src.domain.repositories.product_repository import get_products_by_id
from src.domain.repositories.rule_product_repository import delete_by_rule_ids
from src.domain.repositories.rule_repository import (
    delete_by_ids,
    get_all,
    get_by_rule_ids,
    save,
)
from src.domain.rule_product_service import (
    create_rule_product,
    get_products_by_rule_id,
    get_rule_ids,
)
from src.infra.string_utils import slugify


def create_new_rule(product_list, recommended_product):
    products = [find_or_create_product(product) for product in product_list]
    recommended_product = find_or_create_product(recommended_product)

    rule = Rule(recommended_product=recommended_product)
    rule = save(rule)

    for product in products:
        create_rule_product(rule, product)


def get_all_rules():
    formatted_rules = []
    all_rules = get_all()

    for rule in all_rules:
        rule_product_list = get_products_by_rule_id(rule.rule_id)
        product_id_list = [
            rule_product.product_id for rule_product in rule_product_list
        ]

        product_list = get_products_by_id(product_id_list)
        product_list = [product.product_name for product in product_list]

        formatted_rules.append(
            {
                "product_list": ", ".join(product_list),
                "recommended_product": rule.recommended_product.product_name,
                "rule_id": rule.rule_id,
            }
        )

    return formatted_rules


def delete_rules(rule_ids):
    delete_by_rule_ids(rule_ids)
    delete_by_ids(rule_ids)


def get_recommended_products(product_list):
    products = __find_or_create_products(product_list)
    slugified_product_list = [slugify(product) for product in product_list]

    product_ids = [product.product_id for product in products]
    matching_rule_ids = get_rule_ids(product_ids)
    matching_rules = get_by_rule_ids(matching_rule_ids)

    if len(matching_rules) == 0:  # no recommendations
        return []

    # return just the recommended_product field
    recommended_products = [
        rule.recommended_product for rule in matching_rules if rule.recommended_product
    ]

    # if the recommend product is already in the chart dont add to recommended list
    recommended_products = [
        recommended_product
        for recommended_product in recommended_products
        if recommended_product.product_slug not in slugified_product_list
    ]

    # remove duplicated products
    return list(
        set(
            [
                recommended_product.product_name
                for recommended_product in recommended_products
            ]
        )
    )


def __find_or_create_products(product_list):
    return [find_or_create_product(product) for product in product_list]
