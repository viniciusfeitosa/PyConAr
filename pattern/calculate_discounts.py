# -*- coding: utf-8 -*-
from discounts import DiscountPersonal, DiscountJuridical, \
    DiscountJuridicalWithStatus2, NoneDiscount


class CalculateDiscount(object):

    def calculate(self, user):
        return DiscountPersonal(
            DiscountJuridical(
                DiscountJuridicalWithStatus2(
                    NoneDiscount))).calculate(user)
