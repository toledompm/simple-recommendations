from src.domain.db.config import session
from src.domain.entities.transaction import Transaction


def save(transaction: Transaction) -> Transaction:
    session.add(transaction)
    session.commit()
    get_all.clear_cache()
    return transaction


def delete_by_ids(transaction_ids: list[int]):
    for transaction_id in transaction_ids:
        session.query(Transaction).filter(
            Transaction.transaction_id == transaction_id
        ).delete()

    session.commit()
    get_all.clear_cache()


def get_all() -> list[Transaction]:
    return session.query(Transaction).all()


def get_by_transaction_ids(transaction_ids: list[int]) -> list[Transaction]:
    return (
        session.query(Transaction)
        .filter(Transaction.transaction_id.in_(transaction_ids))
        .all()
    )
