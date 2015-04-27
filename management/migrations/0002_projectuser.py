# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
                ('owner', models.BooleanField(default=False, verbose_name=b'Owner')),
                ('project', models.ForeignKey(verbose_name=b'Project', to='management.Project')),
                ('user', models.ForeignKey(verbose_name=b'User', to='basic.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
