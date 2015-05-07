# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Role name')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=140, verbose_name=b'Team name')),
                ('logo', models.FileField(null=True, upload_to=b'teams/', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('team', models.ForeignKey(related_name='users', verbose_name=b'Team', to='hierarchy.Team')),
                ('user', models.ForeignKey(related_name='teams', verbose_name=b'User', to='basic.User')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='role',
            name='team',
            field=models.ForeignKey(verbose_name=b'Team', to='hierarchy.Team'),
            preserve_default=True,
        ),
    ]
