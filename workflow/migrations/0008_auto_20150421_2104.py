# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_auto_20150421_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='parent_id',
            field=models.ForeignKey(verbose_name='Parent process', null=True, to='workflow.Process'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stagemessage',
            name='reply_to',
            field=models.ForeignKey(verbose_name='Reply to', null=True, to='workflow.StageMessage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskmessage',
            name='reply_to',
            field=models.ForeignKey(verbose_name='Reply to', null=True, to='workflow.TaskMessage'),
            preserve_default=True,
        ),
    ]
