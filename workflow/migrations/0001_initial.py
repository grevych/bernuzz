# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Process name')),
                ('description', models.CharField(max_length=300, verbose_name=b'Description')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('parent_id', models.ForeignKey(verbose_name=b'Parent process', blank=True, to='workflow.Process', null=True)),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'Added on')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('process', models.ForeignKey(related_name='projects', verbose_name=b'Parent Process', to='workflow.Process')),
                ('project', models.ForeignKey(related_name='processes', verbose_name=b'Project', to='management.Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Stage name')),
                ('description', models.CharField(max_length=200, verbose_name=b'Stage description')),
                ('responsible', models.IntegerField(verbose_name=b'Responsible')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Start time')),
                ('end_time', models.DateTimeField(null=True, verbose_name=b'End date', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('process', models.ForeignKey(related_name='stages', verbose_name=b'Process', to='workflow.Process')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StageMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=500, verbose_name=b'Message')),
                ('parent_id', models.IntegerField(verbose_name=b'In reply to')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Announcement Date')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('reply_to', models.ForeignKey(verbose_name=b'Reply to', to='workflow.StageMessage', null=True)),
                ('stage', models.ForeignKey(verbose_name=b'Stage', to='workflow.Stage')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=300, verbose_name=b'Task')),
                ('responsible', models.IntegerField(verbose_name=b'Responsible')),
                ('completed', models.BooleanField(default=False, verbose_name=b'Completed')),
                ('completed_by', models.IntegerField(verbose_name=b'Completed by')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Start time')),
                ('end_time', models.DateTimeField(null=True, verbose_name=b'End date', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('stage', models.ForeignKey(related_name='tasks', verbose_name=b'Stage', to='workflow.Stage')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=500, verbose_name=b'Message')),
                ('parent_id', models.IntegerField(verbose_name=b'In reply to')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Announcement date')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('reply_to', models.ForeignKey(verbose_name=b'Reply to', to='workflow.TaskMessage', null=True)),
                ('task', models.ForeignKey(verbose_name=b'Task', to='workflow.Task')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
    ]
