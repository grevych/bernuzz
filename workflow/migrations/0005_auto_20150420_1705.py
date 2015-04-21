# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0004_auto_20150420_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='stagemessage',
            name='parent_id',
            field=models.IntegerField(verbose_name='In reply to', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskmessage',
            name='parent_id',
            field=models.IntegerField(verbose_name='In reply to', default=0),
            preserve_default=False,
        ),
    ]
