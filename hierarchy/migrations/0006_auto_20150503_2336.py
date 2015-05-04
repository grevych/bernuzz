# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0005_userrole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrole',
            name='role',
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
        migrations.RemoveField(
            model_name='role',
            name='project',
        ),
        migrations.AddField(
            model_name='role',
            name='team',
            field=models.ForeignKey(default=1, verbose_name=b'Team', to='hierarchy.Team'),
            preserve_default=False,
        ),
    ]
