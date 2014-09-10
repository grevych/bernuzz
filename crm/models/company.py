# -*- encoding:utf-8 -*-

from crm.core import db


class Company(db.Document):
    id = db.IntField(primary_key=True, required=True)
    name = db.StringField()
    direction = db.StringField()

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_direction(self):
        return self.direction

    def set_direction(self, dir):
        self.direction = dir
        