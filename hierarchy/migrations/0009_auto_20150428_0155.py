# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0008_auto_20150428_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(unique=True, max_length=140, verbose_name=b'Team name'),
            preserve_default=True,
        ),
    ]
