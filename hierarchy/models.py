# -*- coding: utf-8 -*-

from django.db import models


class Team(models.Model):
    name = models.CharField('Team name', max_length=140)
    logo = models.CharField('Team logo', max_length=140, blank=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return self.name


class TeamMember(models.Model):
    user = models.ForeignKey('basic.User', verbose_name='User', related_name='teams')
    team = models.ForeignKey('Team', verbose_name='Team', related_name='users')
    #date = models.DateField()
    active = models.BooleanField('Active', default=True)
    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return '%s - %s' % (self.user.user.username, self.team.name)


class Role(models.Model):
    name = models.CharField('Role name', max_length=140)
    team = models.ForeignKey('Team', verbose_name='Team')
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return self.name