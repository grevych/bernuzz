# -*- encoding:utf-8 -*-

import zope.interface

from crm.core import db
from .salesman import Salesman


class TeamLeader(db.Document):
    zope.interface.implements(Salesman)

    def register_sale(self, sale):
        pass

    def complete_task(self, task):
        pass

    def create_process(self):
        pass

    def assign_process(self):
        pass
