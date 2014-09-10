# -*- encoding:utf-8 -*-

from crm.core import db
from .sale import Sale
from .team_member import TeamMember
from .team_leader import TeamLeader


class Team(db.Document):
    __id__ = db.IntField(
        primary_key=True,
        required=True)
    __name__ = db.StringField()
    __team_members__ = db.ListReference(
        db.FieldReference(TeamMember))
    __team_leader__ = db.ReferenceField(TeamLeader)
    __sales__ = db.ListReference(
        db.FieldReference(Sale))

    def get_id(self):
        return self.__id__

    def set_id(self, id):
        self.__id__ = id

    def get_name(self):
        return self.__name__

    def set_name(self, name):
        self.__name__ = name

    def add_team_member(self):
        pass

    def remove_team_member(self):
        pass

    def get_team_members(self):
        return self.__team_members__

    def set_team_leader(self, team_leader):
        self.__team_leader__ = team_leader

    def get_team_leader(self):
        return self.__team_leader__

    def remove_team_leader(self):
        pass

    def add_sale(self):
        pass

    def remove_sale(self):
        pass
