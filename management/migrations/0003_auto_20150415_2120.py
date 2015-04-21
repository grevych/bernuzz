# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_project_parent_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Added on')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('college', models.ForeignKey(to='management.College', verbose_name='College')),
                ('project', models.ForeignKey(to='management.Project', verbose_name='Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Added on')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('project', models.ForeignKey(to='management.Project', verbose_name='Project')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Announcements',
            new_name='Announcement',
        ),
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.RemoveField(
            model_name='collegeprojects',
            name='college',
        ),
        migrations.RemoveField(
            model_name='collegeprojects',
            name='project',
        ),
        migrations.DeleteModel(
            name='CollegeProjects',
        ),
        migrations.RemoveField(
            model_name='projectskills',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectskills',
            name='skill',
        ),
        migrations.DeleteModel(
            name='ProjectSkills',
        ),
        migrations.AddField(
            model_name='projectskill',
            name='skill',
            field=models.ForeignKey(to='management.Skill', verbose_name='Skill'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='projectprivacy',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectstatus',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='privacy',
            field=models.ForeignKey(verbose_name='Project Privacy', to='management.ProjectPrivacy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(verbose_name='Project Status', to='management.ProjectStatus'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, verbose_name='End Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='parent_id',
            field=models.ForeignKey(null=True, verbose_name='Parent Project', to='management.Project'),
            preserve_default=True,
        ),
    ]
