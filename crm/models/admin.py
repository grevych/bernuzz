# -*- encoding:utf-8 -*-

from crm.core import db
from .user import User
from .team import Team


class Admin(db.Document, User):

    teams = db.ListReference(db.ReferenceFiedl(Team))

    def add_team(self):
        pass

    def remove_team(self):
        pass

    def get_teams(self):
        return self.teams

    def get_all_sales_status(self):
        pass

    def get_team_status(self, team):
        pass
