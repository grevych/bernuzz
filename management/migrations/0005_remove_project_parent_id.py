# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20150420_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='parent_id',
        ),
    ]
