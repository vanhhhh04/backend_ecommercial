from flask import Flask,Blueprint
from src.api.product import views as product_view 

def create_app():

    app = Flask(__name__)
    register_blueprints(app)
    return app 

def register_blueprints(app):

    app.register_blueprint(product_view.product)

