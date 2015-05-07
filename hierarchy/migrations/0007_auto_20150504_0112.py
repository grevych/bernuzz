# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0006_auto_20150503_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='team',
            field=models.ForeignKey(verbose_name=b'Team', to='hierarchy.Team', null=True),
            preserve_default=True,
        ),
    ]
