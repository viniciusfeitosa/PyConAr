# -*- coding: utf-8 -*-


class DiscountPersonal(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, user):
        if user.user_type == 'personal':
            return user.product_price * 0.07
        else:
            return self.__next_discount.calculate(user)


class DiscountJuridical(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, user):
        if user.user_type == 'juridical':
            return user.product_price * 0.03
        else:
            return self.__next_discount.calculate(user)


class DiscountJuridicalWithStatus2(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, user):
        if user.user_type == 'juridical' and user.status == 2:
            return user.product_price * 0.05
        else:
            return self.__next_discount.calculate(user)


class NoneDiscount(object):

    def calculate(self, user):
        return 0
