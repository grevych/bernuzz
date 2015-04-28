# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
        ('management', '0002_projectuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectuser',
            options={'permissions': ()},
        ),
        migrations.RemoveField(
            model_name='projectuser',
            name='active',
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(verbose_name=b'Team', blank=True, to='hierarchy.Team', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(unique=True, max_length=200, verbose_name=b'Project name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='parent_id',
            field=models.ForeignKey(verbose_name=b'Parent project', blank=True, to='management.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='project',
            field=models.ForeignKey(related_name='users', verbose_name=b'Project', to='management.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='user',
            field=models.ForeignKey(related_name='projects', verbose_name=b'User', to='basic.User'),
            preserve_default=True,
        ),
    ]
