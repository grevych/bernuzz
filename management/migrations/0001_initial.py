# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=140, verbose_name='Subject')),
                ('message', models.CharField(max_length=500, verbose_name='Message')),
                ('date_time', models.DateTimeField(verbose_name='Announcement Date', auto_now_add=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140, verbose_name='Institution Name')),
                ('campus', models.CharField(max_length=140, verbose_name='Campus')),
                ('city', models.CharField(max_length=140, verbose_name='City')),
                ('state', models.CharField(max_length=140, verbose_name='State')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CollegeProjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('college', models.ForeignKey(verbose_name='College', to='management.College')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Project Name')),
                ('area', models.CharField(max_length=200, verbose_name='Area')),
                ('logo', models.CharField(blank=True, max_length=140, verbose_name='Project Logo')),
                ('start_date', models.DateField(verbose_name='Start Date', auto_now_add=True)),
                ('end_date', models.DateField(blank=True, verbose_name='Start Date', null=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectPrivacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Project Privacy')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('project', models.ForeignKey(verbose_name='Project', to='management.Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectSkills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('project', models.ForeignKey(verbose_name='Project', to='management.Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140, verbose_name='Project Status')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('project', models.ForeignKey(verbose_name='Project', to='management.Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140, verbose_name='Skill Name')),
                ('description', models.CharField(max_length=300, verbose_name='Skill Description')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectskills',
            name='skill',
            field=models.ForeignKey(verbose_name='Skill', to='management.Skills'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='collegeprojects',
            name='project',
            field=models.ForeignKey(verbose_name='Project', to='management.Project'),
            preserve_default=True,
        ),
    ]
