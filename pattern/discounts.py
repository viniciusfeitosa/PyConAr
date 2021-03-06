# -*- coding: utf-8 -*-


class DiscountPersonal(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, user):
        if user.user_type == 'personal':
            return user.product_price * 0.07
        else:
            return self.__next_discount.calculate(user)


class DiscountJuridicalWithStatus1(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, user):
        if user.user_type == 'juridical' and user.status_user == 1:
            return user.product_price * 0.03
        else:
            return self.__next_discount.calculate(user)


class DiscountJuridicalWithStatus2(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, user):
        if user.user_type == 'juridical' and user.status_user == 2:
            return user.product_price * 0.05
        else:
            return self.__next_discount.calculate(user)


class DiscountJuridicalWithStatus3(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, user):
        if user.user_type == 'juridical' and user.status_user == 3:
            return user.product_price * 0.08
        else:
            return self.__next_discount.calculate(user)


class DiscountNone(object):

    def calculate(self, user):
        return 0
