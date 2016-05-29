# -*- coding: utf-8 -*-


class CalculateTax(object):

    def calculate(self, user, tax):
        if tax == 'ICMS':
            return user.product_price * 0.1
        elif tax == 'ICPP':
            return user.product_price * 0.3
        elif tax == 'ISS':
            return user.product_price * 0.5
        elif tax == 'IPCA':
            if user.product_price > 100:
                return user.product_price * 0.25
            else:
                return user.product_price * 0.05
        elif tax == 'XIMBINHA':
            if user.product_price > 100:
                return user.product_price * 0.15
            else:
                return user.product_price * 0.02
