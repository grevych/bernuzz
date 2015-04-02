from django.db import models


class Teams(models.Model):
    name = models.CharField("Team name", max_length=140)
    logo = models.CharField("Team Logo", max_length=140, blank=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return self.name


class TeamMembers(models.Model):
    user = models.ForeignKey("basic.Users", verbose_name="User")
    team = models.ForeignKey("Teams", verbose_name="Team")
    active = models.BooleanField("Active", default=True)
    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return "%s - %s" % (self.user.name, self.team.name)


class Roles(models.Model):
    name = models.CharField("Role name", max_length=140)
    team = models.ForeignKey("Teams", verbose_name="Team")
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return self.name