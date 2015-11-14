# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Rate(object):
    def __init__(self, other_rate=None):
        self.__other_rate = other_rate

    def calc_other_rate(self, user):
        if self.__other_rate is None:
            return 0
        else:
            return self.__other_rate.calculate(user)

    @abstractmethod
    def calculate(user):
        pass


class RateWithCondition(Rate):
    __metaclass__ = ABCMeta

    def calculate(self, user):
        if self.use_max_rate(user):
            return self.max_rate(user)
        else:
            return self.min_rate(user)

    @abstractmethod
    def use_max_rate(self, user):
        pass

    @abstractmethod
    def max_rate(self, user):
        pass

    @abstractmethod
    def min_rate(self, user):
        pass


# Decorator Python
def ipvx(func):
    def wrapper(self, user):
        return func(self, user) + 0.1
    return wrapper


class ICMS(Rate):

    @ipvx
    def calculate(self, user):
        return user.product_price * 0.1 + self.calc_other_rate(user)


class ICPP(Rate):
    def calculate(self, user):
        return user.product_price * 0.3 + self.calc_other_rate(user)


class ISS(Rate):
    def calculate(self, user):
        return user.product_price * 0.5 + self.calc_other_rate(user)


class IPCA(RateWithCondition):

    def use_max_rate(self, user):
        return user.product_price > 100

    def max_rate(self, user):
        return user.product_price * 0.25 + self.calc_other_rate(user)

    def min_rate(self, user):
        return user.product_price * 0.05 + self.calc_other_rate(user)


class IKCV(RateWithCondition):

    def use_max_rate(self, user):
        return user.product_price > 100

    def max_rate(self, user):
        return user.product_price * 0.15 + self.calc_other_rate(user)

    def min_rate(self, user):
        return user.product_price * 0.02 + self.calc_other_rate(user)
