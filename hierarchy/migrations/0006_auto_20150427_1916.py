# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0005_auto_20150427_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.FileField(upload_to=b'static/media/teams/'),
            preserve_default=True,
        ),
    ]
