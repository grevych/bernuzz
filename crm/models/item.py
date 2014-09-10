# -*- encoding:utf-8 -*-

from crm.core import db


class Item(db.Document):
    __id__ = db.IntField(
        primary_key=True,
        required=True)
    __name__ = db.StringField()
    __description__ = db.StringField()
    __base_price__ = db.FloatField()

    def get_id(self):
        return self.__id__

    def set_id(self, id):
        self.__id__ = id

    def get_name(self):
        return self.__name__

    def set_name(self, name):
        self.__name__ = name

    def get_description(self):
        return self.__description__

    def set_description(self, desc):
        self.__description__ = desc

    def get_base_price(self):
        return self.__base_price__

    def set_base_price(self, price):
        self.__base_price__ = price
