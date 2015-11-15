# -*- coding: utf-8 -*-
from discounts import DiscountPersonal, \
    DiscountJuridicalWithStatus1, \
    DiscountJuridicalWithStatus2, \
    DiscountJuridicalWithStatus3, DiscountNone


class CalculateDiscount(object):

    def calculate(self, user):
        return DiscountPersonal(
            DiscountJuridicalWithStatus1(
                DiscountJuridicalWithStatus2(
                    DiscountJuridicalWithStatus3(
                        DiscountNone)))).calculate(user)
