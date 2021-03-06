# -*- coding: utf-8 -*-


class CalculateDiscount(object):

    def calculate(self, user):
        if user.user_type == 'personal':
            return user.product_price * 0.1
        elif user.user_type == 'juridical' and user.status_user == 1:
            return user.product_price * 0.03
        elif user.user_type == 'juridical' and user.status_user == 2:
            return user.product_price * 0.05
        elif user.user_type == 'juridical' and user.status_user == 3:
            return user.product_price * 0.08
