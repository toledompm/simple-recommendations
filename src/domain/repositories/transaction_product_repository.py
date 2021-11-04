from src.domain.db.config import session
from src.domain.entities.transaction_product import TransactionProduct


def save(transaction_product: TransactionProduct) -> TransactionProduct:
    session.add(transaction_product)
    session.commit()
    return transaction_product


def get_all_transaction_product_ids_by_transaction() -> dict[int, set[int]]:
    transactions = {}

    query = f"""
    select
        t.transaction_id,
        p.product_id
    from
        transactions t
    inner join
        transaction_products tp on
        tp.transaction_id = t.transaction_id
    inner join
        products p
        on p.product_id = tp.product_id
    group by t.transaction_id, p.product_id;
    """

    all: list[tuple[int]] = session.execute(query).all()

    for transaction in all:
        trans_id, prod_id = transaction

        if transactions.get(trans_id):
            transactions[trans_id] = transactions.get(trans_id).union([prod_id])
        else:
            transactions[trans_id] = set([prod_id])
    return transactions
