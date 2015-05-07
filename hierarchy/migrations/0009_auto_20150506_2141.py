# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
        ('hierarchy', '0008_auto_20150506_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('role', models.ForeignKey(verbose_name=b'Role', to='hierarchy.Role')),
                ('user', models.ForeignKey(verbose_name=b'User', to='basic.User')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='role',
            name='team',
            field=models.ForeignKey(verbose_name=b'Team', blank=True, to='hierarchy.Team', null=True),
            preserve_default=True,
        ),
    ]
