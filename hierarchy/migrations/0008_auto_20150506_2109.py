# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0007_auto_20150504_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='team',
            field=models.ForeignKey(verbose_name=b'Team Member', blank=True, to='hierarchy.TeamMember', null=True),
            preserve_default=True,
        ),
    ]
