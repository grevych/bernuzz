# -*- encoding:utf-8 -*-

from crm.core import db
from .offer import Offer
from .process import Process
from .customer import Customer


STATUS_OP = ('Abierta',
             'En espera',
             'Cancelada',
             'Cerrada')


class Sale(db.Document):
    __id__ = db.IntField(
        primary_key=True,
        required=True)
    __status__ = db.StringField(
        choices=STATUS_OP)
    __process__ = db.ReferenceField(Process)
    __offers__ = db.ListField(
        db.ReferenceField(Offer))
    __customer__ = db.ReferenceField(Customer)

    def get_id(self):
        return self.__id__

    def set_id(self, id):
        self.__id__ = id

    def get_process(self):
        return self.__process__

    def set_process(self, process):
        self.__process__ = process

    def add_offer(self, offer):
        pass

    def remove_offer(self, offer):
        pass

    def get_offers(self):
        return self.__offers__

    def get_latest_offer(self):
        pass

    def get_status(self):
        return self.__status__

    def get_customer(self):
        return self.__customer__

    def set_customer(self, customer):
        self.__customer__ = customer
