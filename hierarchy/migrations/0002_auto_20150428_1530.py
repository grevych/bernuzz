# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(related_name='users', verbose_name=b'Team', to='hierarchy.Team'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teammember',
            name='user',
            field=models.ForeignKey(related_name='teams', verbose_name=b'User', to='basic.User'),
            preserve_default=True,
        ),
    ]
