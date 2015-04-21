# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140, verbose_name='Process Name')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectProcesses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('process', models.ForeignKey(verbose_name='Parent Process', to='workflow.Process')),
                ('project', models.ForeignKey(verbose_name='Project', to='management.Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Stage Name')),
                ('description', models.CharField(max_length=200, verbose_name='Stage Description')),
                ('responsible', models.IntegerField(verbose_name='Responsible')),
                ('start_time', models.DateTimeField(verbose_name='Start Time', auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, verbose_name='End Date', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('process', models.ForeignKey(verbose_name='Process', to='workflow.Process')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StageMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=500, verbose_name='Message')),
                ('parent_id', models.IntegerField(verbose_name='In reply to')),
                ('date_time', models.DateTimeField(verbose_name='Announcement Date', auto_now_add=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('reply_to', models.ForeignKey(to='workflow.StageMessage', null=True, verbose_name='Reply to')),
                ('stage', models.ForeignKey(verbose_name='Stage', to='workflow.Stage')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300, verbose_name='Task')),
                ('responsible', models.IntegerField(verbose_name='Responsible')),
                ('completedBy', models.IntegerField(verbose_name='Completed By')),
                ('start_time', models.DateTimeField(verbose_name='Start Time', auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, verbose_name='End Date', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('stage', models.ForeignKey(verbose_name='Stage', to='workflow.Stage')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=500, verbose_name='Message')),
                ('parent_id', models.IntegerField(verbose_name='In reply to')),
                ('date_time', models.DateTimeField(verbose_name='Announcement Date', auto_now_add=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('reply_to', models.ForeignKey(to='workflow.TaskMessage', null=True, verbose_name='Reply to')),
                ('task', models.ForeignKey(verbose_name='Task', to='workflow.Task')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
    ]
