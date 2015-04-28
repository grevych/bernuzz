# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0005_auto_20150420_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completedBy',
        ),
        migrations.AddField(
            model_name='task',
            name='completed_by',
            field=models.IntegerField(default=0, verbose_name='Completed by'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='process',
            name='name',
            field=models.CharField(verbose_name='Process name', max_length=140),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='process',
            name='parent_id',
            field=models.ForeignKey(null=True, verbose_name='Parent process', to='workflow.Process'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stage',
            name='description',
            field=models.CharField(verbose_name='Stage description', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stage',
            name='end_time',
            field=models.DateTimeField(null=True, blank=True, verbose_name='End date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stage',
            name='name',
            field=models.CharField(verbose_name='Stage name', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stage',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Start time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(null=True, blank=True, verbose_name='End date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Start time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskmessage',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Announcement date'),
            preserve_default=True,
        ),
    ]
