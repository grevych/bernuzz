# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140, verbose_name='Role name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140, verbose_name='Team name')),
                ('logo', models.CharField(blank=True, max_length=140, verbose_name='Team Logo')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='teammembers',
            name='team',
            field=models.ForeignKey(verbose_name='Team', to='hierarchy.Teams'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teammembers',
            name='user',
            field=models.ForeignKey(verbose_name='User', to='basic.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='roles',
            name='team',
            field=models.ForeignKey(verbose_name='Team', to='hierarchy.Teams'),
            preserve_default=True,
        ),
    ]
