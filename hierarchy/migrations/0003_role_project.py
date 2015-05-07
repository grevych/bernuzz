# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20150502_2355'),
        ('hierarchy', '0002_auto_20150503_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='project',
            field=models.ForeignKey(default=0, verbose_name=b'In Project', to='management.Project'),
            preserve_default=False,
        ),
    ]
