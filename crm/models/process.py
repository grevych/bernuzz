# -*- encoding:utf-8 -*-

from crm.core import db
from .stage import StageTemplate
from .company import Company


class ProcessTemplate(db.Document):
    __name__ = db.StringField(
        max_length=40,
        required=True)
    __description__ = db.StringField(
        max_length=140,
        required=True)
    __company__ = db.ReferenceField(Company)
    __stages__ = db.ListField(
        db.ReferenceField(StageTemplate))

    meta = {
        'allow_inheritance': True
    }

    def get_name(self):
        return self.__name__

    def get_description(self):
        return self.__description__

    def get_company(self):
        return self.__company__

    def get_stages(self):
        return self.__stages__


class Process(db.Document, ProcessTemplate):
    __template__ = db.ReferenceField(ProcessTemplate)
