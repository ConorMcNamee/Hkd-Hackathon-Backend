import os

from flask import Flask, Blueprint, request

def create_app():
    app = Flask(__name__)

    from backend import db
    db.init_db()

    from backend.routes import mod
    app.register_blueprint(mod)

    return app


if __name__ == '__main__':
    create_app()