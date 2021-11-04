from src.domain.entities.product import Product
from src.domain.db.config import session


def save(product: Product) -> Product:
    session.add(product)
    session.commit()
    return product


def get_all_except(product_ids: list[int]) -> list[Product]:
    return session.query(Product).filter(Product.product_id.notin_(product_ids)).all()


def get_by_slug(slug: str) -> Product:
    return session.query(Product).filter(Product.product_slug == slug).first()
