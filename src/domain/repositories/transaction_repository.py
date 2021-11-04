from src.domain.db.config import session
from src.domain.entities.transaction import Transaction


def save(transaction: Transaction) -> Transaction:
    session.add(transaction)
    session.commit()
    return transaction
