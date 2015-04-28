# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, related_name='member')
    enrollment = models.CharField('Enrollment', max_length=15)
    career = models.CharField('Career', max_length=50)
    active = models.BooleanField('Active', default=True)

    def __unicode__(self):
        return self.user.username


