# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_log', '0005_auto_20170313_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='request_method',
            field=models.CharField(verbose_name='http method', max_length=10, db_index=True),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='response_code',
            field=models.CharField(verbose_name='response code', max_length=3, db_index=True),
        ),
    ]
