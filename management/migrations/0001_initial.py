# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=140, verbose_name=b'Subject')),
                ('message', models.CharField(max_length=500, verbose_name=b'Message')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Announcement date')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Institution name')),
                ('campus', models.CharField(max_length=140, verbose_name=b'Campus')),
                ('city', models.CharField(max_length=140, verbose_name=b'City')),
                ('state', models.CharField(max_length=140, verbose_name=b'State')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CollegeProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('college', models.ForeignKey(verbose_name=b'College', to='management.College')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Project name')),
                ('area', models.CharField(max_length=200, verbose_name=b'Area')),
                ('logo', models.CharField(max_length=140, verbose_name=b'Project logo', blank=True)),
                ('start_date', models.DateField(auto_now_add=True, verbose_name=b'Start date')),
                ('end_date', models.DateField(null=True, verbose_name=b'Start date', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('parent_id', models.ForeignKey(verbose_name=b'Parent process', to='management.Project', null=True)),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectPrivacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Project privacy')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('project', models.ForeignKey(verbose_name=b'Project', to='management.Project')),
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
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('process', models.ForeignKey(verbose_name=b'Process', to='workflow.Process')),
                ('project', models.ForeignKey(verbose_name=b'Project', to='management.Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('project', models.ForeignKey(verbose_name=b'Project', to='management.Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Project status')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('project', models.ForeignKey(verbose_name=b'Project', to='management.Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Skill name')),
                ('description', models.CharField(max_length=300, verbose_name=b'Skill description')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectskill',
            name='skill',
            field=models.ForeignKey(verbose_name=b'Skill', to='management.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='collegeproject',
            name='project',
            field=models.ForeignKey(verbose_name=b'Project', to='management.Project'),
            preserve_default=True,
        ),
    ]
