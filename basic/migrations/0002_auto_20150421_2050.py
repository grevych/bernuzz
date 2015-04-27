# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='career',
            field=models.CharField(verbose_name='Career', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='enrollment',
            field=models.CharField(verbose_name='Enrollment', max_length=15),
            preserve_default=True,
        ),
    ]
