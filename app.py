# -*- coding: utf-8 -*-
from user import User
from calculate_rates import CalculateRate
from calculate_discounts import CalculateDiscount
from flask import Flask, request, jsonify, abort
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


@app.route("/calculate_rates", methods=['POST'])
def calculate_rates():
    if not request.json:
        abort(400)
    user = User(request)
    rates = []
    rates.append({'ICMS': CalculateRate().calculate(user, 'ICMS')})
    rates.append({'ICPP': CalculateRate().calculate(user, 'ICPP')})
    rates.append({'ISS': CalculateRate().calculate(user, 'ISS')})
    rates.append({'IPCA': CalculateRate().calculate(user, 'IPCA')})
    rates.append({'IKCV': CalculateRate().calculate(user, 'IKCV')})
    return jsonify(name=user.name, rates=rates), 200


@app.route("/calculate_join_rates", methods=['POST'])
def calculate_join_rates():
    if not request.json:
        abort(400)
    user = User(request)
    rates_joined = []
    icms = CalculateRate().calculate(user, 'ICMS')
    icpp = CalculateRate().calculate(user, 'ICPP')
    iss = CalculateRate().calculate(user, 'ISS')
    ipca = CalculateRate().calculate(user, 'IPCA')
    rates_joined.append({'ICMS with ICPP': icms + icpp})
    rates_joined.append({'ISS with IPCA': iss + ipca})
    return jsonify(name=user.name, rates_joined=rates_joined), 200


@app.route("/calculate_discounts", methods=['POST'])
def calculate_discounts():
    if not request.json:
        abort(400)
    user = User(request)
    discount = (CalculateDiscount().calculate(user))
    return jsonify(name=user.name, discount=discount), 200


if __name__ == "__main__":
    app.run()
