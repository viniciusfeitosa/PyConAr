# -*- coding: utf-8 -*-


class User(object):
    def __init__(self, request):
        self.__name = request.json['name']
        self.__email = request.json['email']
        self.__user_type = request.json['user_type']
        self.__product_price = request.json['product_price']
        self.__product_list = request.json['product_list']
        self.__status_user = request.json['status_user']

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def user_type(self):
        return self.__user_type

    @property
    def product_price(self):
        return self.__product_price

    @property
    def product_list(self):
        return self.__product_list

    @property
    def status_user(self):
        return self.__status_user
