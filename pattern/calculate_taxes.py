# -*- coding: utf-8 -*-


class CalculateTax(object):

    def calculate(self, user, rate):
        return rate.calculate(user)
