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


@app.route("/calculate_discounts", methods=['POST'])
def calculate_discounts():
    if not request.json:
        abort(400)
    user = User(request)
    discount = (CalculateDiscount().calculate(user))
    return jsonify(name=user.name, discount=discount), 200


if __name__ == "__main__":
    app.run(debug=True)
