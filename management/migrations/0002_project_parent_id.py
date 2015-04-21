# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='parent_id',
            field=models.ForeignKey(null=True, to='management.Project', verbose_name='Parent Process'),
            preserve_default=True,
        ),
    ]
