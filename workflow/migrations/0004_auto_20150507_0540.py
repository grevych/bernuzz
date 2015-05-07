# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
        ('workflow', '0003_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='responsible',
            field=models.ForeignKey(related_name='processes', default=1, verbose_name=b'Responsible', to='basic.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stage',
            name='responsible',
            field=models.ForeignKey(related_name='stages', verbose_name=b'Responsible', to='basic.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='completed_by',
            field=models.ForeignKey(related_name='completed', verbose_name=b'completed By', to='basic.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='responsible',
            field=models.ForeignKey(related_name='tasks', verbose_name=b'Responsible', to='basic.User'),
            preserve_default=True,
        ),
    ]
