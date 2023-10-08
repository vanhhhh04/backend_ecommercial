from flask import Flask,Blueprint
from src.api.product import views as product_view 
from src.api.extensions import cache, cors


def create_app():

    app = Flask(__name__)
    register_blueprints(app)
    return app 



def register_blueprints(app: Flask):
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(product_view.product, origins=origins)

    app.register_blueprint(product_view.product)

def register_extensions(app):
    """Register Flask extensions."""

    cache.init_app(app)
    cors.init_app(app)