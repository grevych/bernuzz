# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_auto_20150507_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='sub',
            field=models.ForeignKey(related_name='parent', verbose_name=b'Sub Process', blank=True, to='workflow.Process', null=True),
            preserve_default=True,
        ),
    ]
