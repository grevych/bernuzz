# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
        ('hierarchy', '0004_auto_20150503_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
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
    ]
