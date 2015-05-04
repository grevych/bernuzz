# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='team',
        ),
        migrations.AddField(
            model_name='role',
            name='team_member',
            field=models.ForeignKey(default=0, verbose_name=b'Team Member', to='hierarchy.TeamMember'),
            preserve_default=False,
        ),
    ]
