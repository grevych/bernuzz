# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0003_role_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='team_member',
        ),
        migrations.AlterField(
            model_name='role',
            name='project',
            field=models.ForeignKey(verbose_name=b'In Project', to='management.Project', null=True),
            preserve_default=True,
        ),
    ]
