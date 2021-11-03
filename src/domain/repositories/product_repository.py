from src.infra.cache import custom_lru_cache
from src.domain.entities.product import Product
from src.domain.db.config import session


def save(product: Product):
    session.add(product)
    session.commit()
    get_by_slug.cache_remove(product.product_slug)
    return product


def get_products_by_id(product_ids: list):
    return session.query(Product).filter(Product.product_id.in_(product_ids)).all()


@custom_lru_cache
def get_by_slug(slug):
    return session.query(Product).filter(Product.product_slug == slug).first()
