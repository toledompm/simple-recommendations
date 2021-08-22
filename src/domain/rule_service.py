from itertools import combinations

from src.domain.entities.rule import Rule
from src.domain.repositories.rule_repository import (
    delete_by_ids,
    get_all,
    save,
)


def create_new_rule(product_list, recommended_product):
    rule_key = __generate_group_key(product_list)
    rule = Rule(rule_key, __pretify(recommended_product))
    return save(rule)


def get_all_rules():
    all_rules = get_all()

    for rule in all_rules:
        rule.product_list = __split_group_key(rule.rule_key)

    return all_rules


def delete_rules(rule_ids):
    delete_by_ids(rule_ids)


def get_recommended_products(product_list):
    all_rule_keys = []
    for combination_length in range(1, len(product_list) + 1):
        partial_combinations = [
            list(x) for x in combinations(product_list, combination_length)
        ]
        all_rule_keys.extend(
            [__generate_group_key(combination) for combination in partial_combinations]
        )

    matching_rules = __get_matching_rules(all_rule_keys)
    if len(matching_rules) == 0:
        return []

    slugified_product_list = [__slugify(product) for product in product_list]

    recommended_products = [
        rule.recommended_product for rule in matching_rules if rule.recommended_product
    ]
    recommended_products = [
        recommended_product
        for recommended_product in recommended_products
        if __slugify(recommended_product) not in slugified_product_list
    ]
    return list(set(recommended_products))


def __get_matching_rules(rule_keys):
    all_rules = get_all()
    return [rule for rule in all_rules if rule.rule_key in rule_keys]


def __split_group_key(group_key):
    slugified_product_list = group_key.split("__")
    return [__unslugify(product) for product in slugified_product_list]


def __generate_group_key(product_list):
    slugified_product_list = [__slugify(product) for product in product_list]
    slugified_product_list.sort()
    return "__".join(slugified_product_list)


def __slugify(text):
    return text.lower().strip().replace(" ", "-")


def __unslugify(slugified_text):
    return __pretify(slugified_text.replace("-", " "))


def __pretify(text):
    return text.strip().title()
