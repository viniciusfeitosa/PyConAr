# -*- coding: utf-8 -*-
from user import User
from calculate_taxes import CalculateTax
from calculate_discounts import CalculateDiscount
from flask import Flask, request, jsonify, abort
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


@app.route("/calculate_tax", methods=['POST'])
def calculate_tax():
    if not request.json:
        abort(400)
    user = User(request)
    taxes = []
    taxes.append({'ICMS': CalculateTax().calculate(user, 'ICMS')})
    taxes.append({'ICPP': CalculateTax().calculate(user, 'ICPP')})
    taxes.append({'ISS': CalculateTax().calculate(user, 'ISS')})
    taxes.append({'IPCA': CalculateTax().calculate(user, 'IPCA')})
    taxes.append({'XIMBINHA': CalculateTax().calculate(user, 'XIMBINHA')})
    return jsonify(name=user.name, taxes=taxes), 200


@app.route("/calculate_join_tax", methods=['POST'])
def calculate_join_tax():
    if not request.json:
        abort(400)
    user = User(request)
    taxes_joined = []
    icms = CalculateTax().calculate(user, 'ICMS')
    icpp = CalculateTax().calculate(user, 'ICPP')
    iss = CalculateTax().calculate(user, 'ISS')
    ipca = CalculateTax().calculate(user, 'IPCA')
    taxes_joined.append({'ICMS with ICPP': icms + icpp})
    taxes_joined.append({'ISS with IPCA': iss + ipca})
    return jsonify(name=user.name, taxes_joined=taxes_joined), 200


@app.route("/calculate_discounts", methods=['POST'])
def calculate_discounts():
    if not request.json:
        abort(400)
    user = User(request)
    discount = (CalculateDiscount().calculate(user))
    return jsonify(name=user.name, discount=discount), 200


if __name__ == "__main__":
    app.run()
