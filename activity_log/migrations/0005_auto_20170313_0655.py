# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_log', '0004_auto_20170309_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='request_url',
            field=models.CharField(max_length=256, verbose_name='url'),
        ),
    ]
