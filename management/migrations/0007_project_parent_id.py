# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20150420_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='parent_id',
            field=models.ForeignKey(to='management.Project', verbose_name='Parent Project', null=True),
            preserve_default=True,
        ),
    ]
