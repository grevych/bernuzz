# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Access Level')),
                ('active', models.BooleanField(default=True, verbose_name=b'Active')),
            ],
            options={
                'permissions': (),
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='ProjectPrivacy',
        ),
        migrations.AddField(
            model_name='project',
            name='access_level',
            field=models.ForeignKey(verbose_name=b'Access Level', blank=True, to='management.AccessLevel', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.FileField(null=True, upload_to=b'projects/images/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Project name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(related_name='projects', verbose_name=b'Team', blank=True, to='hierarchy.Team', null=True),
            preserve_default=True,
        ),
    ]
