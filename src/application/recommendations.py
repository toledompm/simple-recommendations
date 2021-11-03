from src.domain.rule_service import (
    create_new_rule,
    delete_rules,
    get_all_rules,
    get_recommended_products,
)


def save_rule():
    product_list = input(
        "Enter product list separated by '|' (i.e: sugar | honey | ice tea): "
    )
    product_list = product_list.split("|")
    recommended_product = input("Enter recommended product: ")

    create_new_rule(product_list, recommended_product)
    print("Rule created")
    input("Press Enter to continue...")


def list_rules():
    all_rules = get_all_rules()
    for rule in all_rules:
        print(
            f"id: {rule['rule_id']} - Product List: {rule['product_list']} | Recommended Product: {rule['recommended_product']}"
        )

    print("Do you want to delete any rules? [y/N]: ")
    delete_option = input()
    if delete_option == "y":
        ids_to_delete = input(
            "Enter the ids to delete separated by spaces (i.e: 10 20 40): "
        )
        ids_to_delete = ids_to_delete.split(" ")
        delete_rules(ids_to_delete)
        input("Press Enter to continue...")


def recommend():
    product_list = input(
        "Enter product list separated by '|' (i.e: sugar | honey | ice tea): "
    )
    product_list = product_list.split("|")
    recommended_products = get_recommended_products(product_list)
    print(f"Recommended products: {recommended_products}")
    input("Press Enter to continue...")
