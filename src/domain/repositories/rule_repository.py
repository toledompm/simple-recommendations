from src.infra.cache import custom_lru_cache
from src.domain.entities.rule import Rule
from src.domain.db.config import session


def save(rule: Rule):
    session.add(rule)
    session.commit()
    get_all.clear_cache()
    return rule


def delete_by_ids(rule_ids: list):
    for rule_id in rule_ids:
        session.query(Rule).filter(Rule.rule_id == rule_id).delete()

    session.commit()

    get_by_rule_ids.clear_cache()
    get_all.clear_cache()


@custom_lru_cache
def get_all():
    return session.query(Rule).all()


def get_by_rule_ids(rule_ids: list):
    return session.query(Rule).filter(Rule.rule_id.in_(rule_ids)).all()
