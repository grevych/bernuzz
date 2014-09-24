# -*- encoding:utf-8 -*-

from crm.core import db


class TaskTemplate(db.Document):
    __description__ = db.StringField(
        max_length=140,
        required=True)
    __stage_template__ = db.ReferenceField('StageTemplate')

    meta = {
        'allow_inheritance': True
    }

    def get_name(self):
        return self.__name__

    def get_stage(self):
        return self.__stage__


class Task(TaskTemplate):
    __description__ = db.StringField(
        max_length=140,
        required=True)
    __stage__ = db.ReferenceField('Stage')
    __template__ = db.ReferenceField(TaskTemplate)
    __completed__ = db.BooleanField(
        default=False)
    __manager__ = db.ReferenceField('User')
