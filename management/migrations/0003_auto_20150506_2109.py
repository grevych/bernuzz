# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20150502_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectskill',
            name='project',
            field=models.ForeignKey(related_name='skills', verbose_name=b'Project', to='management.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectskill',
            name='skill',
            field=models.ForeignKey(related_name='projects', verbose_name=b'Skill', to='management.Skill'),
            preserve_default=True,
        ),
    ]
