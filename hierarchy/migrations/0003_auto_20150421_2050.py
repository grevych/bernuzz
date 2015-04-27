# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0002_auto_20150415_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.CharField(blank=True, verbose_name='Team logo', max_length=140),
            preserve_default=True,
        ),
    ]
