from src.infra.cache import custom_cache
from src.domain.entities.rule import Rule
from src.domain.db.config import session


def save(rule):
    session.add(rule)
    session.commit()
    get_all.clear_cache()


def delete_by_ids(rule_ids):
    session.query(Rule).filter(Rule.rule_id.in_(rule_ids)).delete()
    session.commit()
    get_all.clear_cache()


@custom_cache
def get_all():
    return session.query(Rule).all()
