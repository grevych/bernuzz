# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0006_auto_20150507_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='sub',
            field=models.ForeignKey(related_name='parent', default=0, verbose_name=b'Sub Process', to='workflow.Process'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stage',
            name='process',
            field=models.ForeignKey(related_name='stages', default=0, verbose_name=b'Process', to='workflow.Process'),
            preserve_default=False,
        ),
    ]
