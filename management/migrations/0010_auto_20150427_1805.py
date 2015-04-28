# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuser',
            name='project',
            field=models.ForeignKey(related_name='users', verbose_name=b'Project', to='management.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='user',
            field=models.ForeignKey(related_name='projects', verbose_name=b'User', to='basic.User'),
            preserve_default=True,
        ),
    ]
