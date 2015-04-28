# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_remove_project_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(to='management.ProjectStatus', verbose_name='Project Status'),
            preserve_default=True,
        ),
    ]
