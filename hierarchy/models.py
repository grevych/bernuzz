# -*- coding: utf-8 -*-

from django.db import models


class Team(models.Model):
    name = models.CharField('Team name', max_length=140, unique=True)
    logo = models.FileField(upload_to='teams/', null=True, blank=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return self.name


class TeamMember(models.Model):
    user = models.ForeignKey('basic.User', verbose_name='User')
    team = models.ForeignKey('Team', verbose_name='Team')
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return '%s - %s' % (self.user.name, self.team.name)


class Role(models.Model):
    name = models.CharField('Role name', max_length=140)
    team = models.ForeignKey('Team', verbose_name='Team')
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return self.name