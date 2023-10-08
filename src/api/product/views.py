from src.api import HttpMethod
from src.api.urls import Endpoint
from flask import Blueprint
product = Blueprint("product", __name__)


@product.route(Endpoint.PRODUCT, methods=[HttpMethod.GET])
def get_all_products():
    return {
        "product_count": 2,
        "articles": [
                {
                    "s": {
                        "bio": "vanh la tui ",
                        "image": '',
                        "name": "vanh1"
                        },
                    "body": "bai1's body ",
                    "created_at": "Wed, 09 Aug 2023 14:31:14 GMT",
                    "favorites_count": 2,
                    "id": 1,
                    "title": "bai1"
                }
                ]
            }
