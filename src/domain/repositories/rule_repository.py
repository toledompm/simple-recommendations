from src.domain.entities.rule import Rule
from src.domain.db.config import session


def save(rule):
    session.add(rule)
    session.commit()


def get_many(rule_keys):
    return session.query(Rule).filter(Rule.rule_key.in_(rule_keys)).all()


def get_all():
    return session.query(Rule).all()


def delete_by_ids(rule_ids):
    session.query(Rule).filter(Rule.rule_id.in_(rule_ids)).delete()
    session.commit()
