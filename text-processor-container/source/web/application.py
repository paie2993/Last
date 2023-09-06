from flask import Flask
from flask_cors import CORS


def create_application():
    app = Flask(__name__)
    CORS(app)

    from web.routes import domain

    app.register_blueprint(domain)
    return app
