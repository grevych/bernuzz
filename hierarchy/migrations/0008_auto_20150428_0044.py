# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0007_auto_20150427_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.FileField(null=True, upload_to=b'teams/', blank=True),
            preserve_default=True,
        ),
    ]
