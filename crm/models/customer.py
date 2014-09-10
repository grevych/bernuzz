# -*- encoding:utf-8 -*-

from crm.core import db
from .user import User
from .sale import Sale


class Customer(db.Document, User):
    sales = db.ListField(db.ReferenceField(Sale))

    def reply_offer(self):
        pass
