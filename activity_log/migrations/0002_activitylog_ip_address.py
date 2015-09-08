# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitylog',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, verbose_name='user IP', blank=True),
        ),
    ]
