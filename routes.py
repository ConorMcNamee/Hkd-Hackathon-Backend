from flask import Blueprint

mod = Blueprint('routes', __name__, url_prefix='/app')

@mod.route('/')
def hello():
    return "Hello World"

@mod.route('/map')
def map_route():
    pass

    #return Lat, Long, Amount, firstname, lastname, datetime

def monthly_spend():
    pass

    # return firstname

def see_fraud_transactions():
    pass