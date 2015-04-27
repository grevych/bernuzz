# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0006_auto_20150421_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='process',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='stagemessage',
            name='reply_to',
        ),
        migrations.RemoveField(
            model_name='taskmessage',
            name='reply_to',
        ),
    ]
