# -*- encoding:utf-8 -*-

from crm.core import db
from .role import Role
from .company import Company


class User(db.Document):
    __first_name__ = db.StringField()
    __last_name__ = db.StringField()
    __email__ = db.EmailField()
    __role__ = db.ReferenceField('Role')
    __company__ = db.ReferenceField('Company')

    meta = {'allow_inheritance': True}

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_company(self):
        return self.company

    def set_company(self, company):
        self.company = company
