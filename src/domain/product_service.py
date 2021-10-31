from src.domain.entities.product import Product
from src.domain.repositories.product_repository import get_by_slug, save
from src.infra.string_utils import pretify, slugify


def find_or_create_product(product_name):
    slug = slugify(product_name)
    prettified_name = pretify(product_name)

    product = get_by_slug(slug)
    if product:
        return product

    product = save(Product(product_name=prettified_name, product_slug=slug))
    return product
