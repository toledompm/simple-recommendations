from src.domain.entities.product import Product
from src.domain.entities.transaction import Transaction
from src.domain.product_service import find_or_create_product
from src.domain.repositories.product_repository import get_all_except
from src.domain.repositories.transaction_product_repository import \
    get_all_transaction_product_ids_by_transaction
from src.domain.repositories.transaction_repository import save
from src.domain.transaction_product_service import create_transaction_product
from src.infra.apriori import confidence, support

ALL_OTHER_PRODUCTS_MIN_SUPPORT = 0.05
MIN_CONFIDENCE = 0.5

class __SupportObject:
    support: float
    product: Product

    def __init__(self, support_value: float, product: Product):
        self.support = support_value
        self.product = product


class __ConfidenceObject:
    product: Product
    associated_product: Product
    confidence: float

    def __init__(
        self,
        product: Product,
        associated_product: Product,
        confidence: float,
        support: float,
    ):
        self.product = product
        self.associated_product = associated_product
        self.confidence = confidence
        self.support = support

    def __to_string__(self):
        return f"{self.product.product_name} -> {self.associated_product.product_name}: c:{self.confidence} - s:{self.support}"


def create_new_transaction(product_name_list: list[str]):
    products = __find_or_create_products(product_name_list)

    transaction = Transaction()
    transaction = save(transaction)

    for product in products:
        create_transaction_product(transaction, product)


def get_recommended_product(product_name_list: str) -> list[__ConfidenceObject]:
    product_ids_by_transaction = get_all_transaction_product_ids_by_transaction()
    products = __find_or_create_products(product_name_list)

    all_other_products = __find_all_other_products(products)
    all_other_products = __prune_by_support(
        all_other_products, product_ids_by_transaction, ALL_OTHER_PRODUCTS_MIN_SUPPORT
    )

    cart_support_list = __generate_support_objects(products, product_ids_by_transaction)
    cart_association_list = __calculate_products_confidence(
        cart_support_list, all_other_products, product_ids_by_transaction
    )

    final_cart_association_list = __prune_by_confidence(cart_association_list, MIN_CONFIDENCE)

    return final_cart_association_list

def __find_or_create_products(product_name_list: str) -> list[Product]:
    return [find_or_create_product(product) for product in product_name_list]


def __find_all_other_products(products: list[Product]) -> list[Product]:
    return get_all_except([product.product_id for product in products])


def __generate_support_objects(
    products: list[Product],
    product_ids_by_transaction: dict[int, set[int]],
    min_support=None,
) -> list[__SupportObject]:
    support_list = []
    for product in products:
        support_value = support(
            product.product_id, product.product_id, product_ids_by_transaction
        )
        if min_support is not None and support_value < min_support:
            continue

        support_obj = __SupportObject(support_value, product)
        support_list.append(support_obj)

    return support_list


def __calculate_products_confidence(
    support_list: list[__SupportObject],
    all_other_products: list[Product],
    product_ids_by_transaction: dict[int, set[int]],
) -> list[__ConfidenceObject]:
    association_list = []
    for product_support in support_list:
        for other_product in all_other_products:
            support_value = support(
                product_support.product.product_id,
                other_product.product_id,
                product_ids_by_transaction,
            )

            confidence_value = confidence(
                product_support.product.product_id,
                other_product.product_id,
                product_ids_by_transaction,
            )

            association_obj = __ConfidenceObject(
                product_support.product,
                other_product,
                confidence_value,
                support_value,
            )

            association_list.append(association_obj)

    return association_list


def __prune_by_support(
    product_list: list[Product], transactions: dict[int, set[int]], min_support: float
) -> list[Product]:
    support_list = __generate_support_objects(product_list, transactions, min_support)
    return [product.product for product in support_list]

def __prune_by_confidence(confidence_list: list[__ConfidenceObject], min_confidence: float) -> list[__ConfidenceObject]:
    return [confidence_object for confidence_object in confidence_list if confidence_object.confidence >= min_confidence]
