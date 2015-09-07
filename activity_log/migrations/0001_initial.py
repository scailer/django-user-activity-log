# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name='user id ')),
                ('user', models.CharField(max_length=256, verbose_name='user')),
                ('request_url', models.CharField(max_length=256, verbose_name='url')),
                ('request_method', models.CharField(max_length=10, verbose_name='http method')),
                ('response_code', models.CharField(max_length=3, verbose_name='response code')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='datetime')),
            ],
            options={
                'verbose_name': 'activity log',
            },
        ),
    ]
