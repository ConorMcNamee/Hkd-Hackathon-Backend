from flask import Blueprint

mod = Blueprint('routes', __name__, url_prefix='/routes')

@mod.route('/')
def hello():
    return "Hello World"

    