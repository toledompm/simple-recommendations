from src.domain.transaction_service import get_recommended_product


def recommend():
    product_list = input(
        "Enter product list separated by '|' (i.e: sugar | honey | ice tea): "
    )
    product_list = product_list.split("|")
    recommended_product = get_recommended_product(product_list)
    print(f"Recommended product: {recommended_product}")
    input("Press Enter to continue...")
