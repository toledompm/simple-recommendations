from src.domain.transaction_service import (create_new_transaction,
                                            get_recommended_product)


def recommend():
    product_list = input(
        "Enter product list separated by '|' (i.e: sugar | honey | ice tea): "
    )
    product_list = product_list.split("|")
    
    recommends_products = get_recommended_product(product_list)
    recommends_products = set([assoc.associated_product.product_name for assoc in recommends_products])

    recommend_products_string = ', '.join(recommends_products)
    
    print("Recommended products:", 'None' if len(recommends_products) == 0 else recommend_products_string)
    
    create_new_transaction(product_list)

    input("Press Enter to continue...")
