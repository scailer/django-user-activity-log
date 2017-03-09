# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activity_log', '0003_activitylog_extra_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='datetime', db_index=True),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='user IP', db_index=True),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='request_url',
            field=models.CharField(db_index=True, verbose_name='url', max_length=256),
        ),
    ]
