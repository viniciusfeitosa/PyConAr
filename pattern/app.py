# -*- coding: utf-8 -*-
from user import User
from calculate_taxes import CalculateTax
from calculate_discounts import CalculateDiscount
from taxes import ICMS, ICPP, ISS, IPCA, XIMBINHA
from flask import Flask, request, jsonify, abort
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


@app.route("/calculate_tax", methods=['POST'])
def calculate_taxes():
    if not request.json:
        abort(400)
    user = User(request)
    taxes = []
    taxes.append(
        {'ICMS': CalculateTax().calculate(user, ICMS())})
    taxes.append(
        {'ICPP': CalculateTax().calculate(user, ICPP())})
    taxes.append(
        {'ISS': CalculateTax().calculate(user, ISS())})
    taxes.append(
        {'IPCA': CalculateTax().calculate(user, IPCA())})
    taxes.append(
        {'XIMBINHA': CalculateTax().calculate(user, XIMBINHA())})
    return jsonify(name=user.name, taxes=taxes), 200


@app.route("/calculate_join_tax", methods=['POST'])
def calculate_join_taxes():
    if not request.json:
        abort(400)
    user = User(request)
    taxes_joined = []
    icms_with_icpp = CalculateTax().calculate(user, ICMS(ICPP()))
    iss_with_ipca = CalculateTax().calculate(user, ISS(IPCA()))
    taxes_joined.append({'ICMS with ICPP': icms_with_icpp})
    taxes_joined.append({'ISS with IPCA': iss_with_ipca})
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
