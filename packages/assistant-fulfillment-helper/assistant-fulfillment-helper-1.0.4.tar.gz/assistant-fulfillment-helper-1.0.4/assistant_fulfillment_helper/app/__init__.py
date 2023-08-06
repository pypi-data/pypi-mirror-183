from flask import Flask

__version__ = '1.0.0'

def create_app():

    app = Flask(__name__)
    app.secret_key = "95692d04d5206db36a1b23bf4e4460fc"

    register_blueprints(app)

    return app


def register_blueprints(app):
    from .routes import server_bp

    app.register_blueprint(server_bp)
