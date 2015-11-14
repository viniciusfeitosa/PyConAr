# -*- coding: utf-8 -*-
from user import User
from calculate_rates import CalculateRate
from calculate_discounts import CalculateDiscount
from rates import ICMS, ICPP, ISS, IPCA, IKCV
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
    rates.append(
        {'ICMS': CalculateRate().calculate(user, ICMS())})
    rates.append(
        {'ICPP': CalculateRate().calculate(user, ICPP())})
    rates.append(
        {'ISS': CalculateRate().calculate(user, ISS())})
    rates.append(
        {'IPCA': CalculateRate().calculate(user, IPCA())})
    rates.append(
        {'IKCV': CalculateRate().calculate(user, IKCV())})
    return jsonify(name=user.name, rates=rates), 200


@app.route("/calculate_join_rates", methods=['POST'])
def calculate_join_rates():
    if not request.json:
        abort(400)
    user = User(request)
    rates_joined = []
    icms_with_icpp = CalculateRate().calculate(user, ICMS(ICPP()))
    iss_with_ipca = CalculateRate().calculate(user, ISS(IPCA()))
    rates_joined.append({'ICMS with ICPP': icms_with_icpp})
    rates_joined.append({'ISS with IPCA': iss_with_ipca})
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
