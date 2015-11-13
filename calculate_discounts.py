# -*- coding: utf-8 -*-


class CalculateDiscount(object):

    def calculate(self, user):
        if user.user_type == 'personal':
            return user.product_price * 0.1
        elif user.user_type == 'juridical':
            return user.product_price * 0.03
        elif user.user_type == 'juridical' and user.status == 2:
            return user.product_price * 0.05
        elif user.user_type == 'juridical' and user.status == 3:
            return user.product_price * 0.08
