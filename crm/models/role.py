# -*- encoding:utf-8 -*-

from crm.core import db
from .permission import Permission


class Role(db.Document):
    id = db.IntField(primary_key=True, required=True)
    name = db.StringField()
    permissions = db.ListField(db.ReferenceField(Permission))

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def add_permission(self):
        pass

    def remove_permission(self):
        pass

    def has_permission(self):
        pass
