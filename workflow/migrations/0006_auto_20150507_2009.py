# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0005_auto_20150507_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='process',
            field=models.ForeignKey(related_name='stages', verbose_name=b'Process', blank=True, to='workflow.Process', null=True),
            preserve_default=True,
        ),
    ]
