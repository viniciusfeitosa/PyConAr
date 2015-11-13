# -*- coding: utf-8 -*-


class CalculateRate(object):

    def calculate(self, user, rate):
        if rate == 'ICMS':
            return user.product_price * 0.1
        elif rate == 'ICPP':
            return user.product_price * 0.3
        elif rate == 'ISS':
            return user.product_price * 0.5
        elif rate == 'IPCA':
            if user.product_price > 100:
                return user.product_price * 0.25
            else:
                return user.product_price * 0.05
        elif rate == 'IKCV':
            if user.product_price > 100:
                return user.product_price * 0.15
            else:
                return user.product_price * 0.02
