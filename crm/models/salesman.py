# -*- encoding:utf-8 -*-

import zope.interface

from .user import User


class Salesman(User, zope.interface.Interface):

    def register_sale(sale):
        "We don't need to call to self"
        pass

    def complete_task(task):
        "We don't need to call to self"
        pass
