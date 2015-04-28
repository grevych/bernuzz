# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20150421_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.OneToOneField(related_name='member', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
