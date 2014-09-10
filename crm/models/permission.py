# -*- encoding:utf-8 -*-

from crm.core import db


class Permission(db.Document):
    id = db.IntField(primary_key=True, required=True)
    name = db.StringField()
    description = db.StringField()

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, desc):
        self.description = desc
