# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_log', '0002_activitylog_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitylog',
            name='extra_data',
            field=models.TextField(null=True, verbose_name='extra data', blank=True),
        ),
    ]
