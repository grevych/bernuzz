# -*- encoding:utf-8 -*-

from crm.core import db


class StageTemplate(db.Document):
    __title__ = db.StringField(
        max_length=40,
        required=True)
    __process_template__ = db.ReferenceField('ProcessTemplate')
    __task_templates__ = db.ListField(
        db.ReferenceField('TaskTemplate'))

    meta = {
        'allow_inheritance': True
    }

    def get_name(self):
        return self.__name__

    def get_process(self):
        return self.__process__

    def get_tasks(self):
        return self.__tasks__


class Stage(db.Document):
    __title__ = db.StringField(
        max_length=40,
        required=True)
    __process__ = db.ReferenceField('Process')
    __tasks__ = db.ListField(
        db.ReferenceField('Task'))
    __template__ = db.ReferenceField('StageTemplate')
    __manager__ = db.ReferenceField('User')
