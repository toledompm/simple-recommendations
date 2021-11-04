from src.domain.entities.product import Product
from src.domain.entities.transaction import Transaction
from src.domain.entities.transaction_product import TransactionProduct
from src.domain.repositories.transaction_product_repository import save


def create_transaction_product(transaction: Transaction, product: Product):
    transaction_product = TransactionProduct(transaction_id=transaction.transaction_id, product_id=product.product_id)
    save(transaction_product)
