# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name='Role name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
        migrations.RemoveField(
            model_name='roles',
            name='team',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='team',
        ),
        migrations.RemoveField(
            model_name='teammembers',
            name='user',
        ),
        migrations.DeleteModel(
            name='TeamMembers',
        ),
        migrations.AddField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(to='hierarchy.Team', verbose_name='Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teammember',
            name='user',
            field=models.ForeignKey(to='basic.User', verbose_name='User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='role',
            name='team',
            field=models.ForeignKey(to='hierarchy.Team', verbose_name='Team'),
            preserve_default=True,
        ),
    ]
