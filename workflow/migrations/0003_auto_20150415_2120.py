# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20150415_2120'),
        ('workflow', '0002_process_parent_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Added on')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('process', models.ForeignKey(to='workflow.Process', verbose_name='Parent Process')),
                ('project', models.ForeignKey(to='management.Project', verbose_name='Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='projectprocesses',
            name='process',
        ),
        migrations.RemoveField(
            model_name='projectprocesses',
            name='project',
        ),
        migrations.DeleteModel(
            name='ProjectProcesses',
        ),
    ]
