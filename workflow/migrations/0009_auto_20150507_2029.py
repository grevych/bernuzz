# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0008_auto_20150507_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_by',
            field=models.ForeignKey(related_name='completed', verbose_name=b'completed By', blank=True, to='basic.User', null=True),
            preserve_default=True,
        ),
    ]
