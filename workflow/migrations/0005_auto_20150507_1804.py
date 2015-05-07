# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0004_auto_20150507_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='due_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 18, 4, 8, 777899, tzinfo=utc), verbose_name=b'Due time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='due_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 18, 4, 24, 715982, tzinfo=utc), verbose_name=b'Due time'),
            preserve_default=False,
        ),
    ]
