from src.domain.transaction_service import get_recommended_product


def recommend():
    product_list = input(
        "Enter product list separated by '|' (i.e: sugar | honey | ice tea): "
    )
    product_list = product_list.split("|")
    # TODO: get recommended product

    input("Press Enter to continue...")
