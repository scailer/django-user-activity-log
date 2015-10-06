# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.apps import apps
from django.dispatch import receiver
from django.db.models.signals import pre_migrate
from django.db import connection
from django.core.management import call_command
from django.conf import settings
from django.db.utils import ProgrammingError

from . import conf


if conf.AUTOCREATE_DB:
    @receiver(pre_migrate, sender=apps.get_app_config('activity_log'))
    def createdb(sender, using, **kwargs):
        db = settings.DATABASES[conf.LOG_DB_KEY]['NAME']
        with connection.cursor() as cursor:
            try:
                cursor.execute("CREATE DATABASE {}".format(db))
            except ProgrammingError:
                pass

        if using == 'default':
            call_command('migrate', database=conf.LOG_DB_KEY)


class ActivityLog(models.Model):
    user_id = models.IntegerField(_('user id '))
    user = models.CharField(_('user'), max_length=256)
    request_url = models.CharField(_('url'), max_length=256)
    request_method = models.CharField(_('http method'), max_length=10)
    response_code = models.CharField(_('response code'), max_length=3)
    datetime = models.DateTimeField(_('datetime'), default=timezone.now)
    extra_data = models.TextField(_('extra data'), blank=True, null=True)
    ip_address = models.GenericIPAddressField(
        _('user IP'), null=True, blank=True)

    class Meta:
        verbose_name = _('activity log')


class UserMixin(models.Model):
    last_activity = models.DateTimeField(
        _('last activity'), default=timezone.now, editable=False)

    def update_last_activity(self):
        self.last_activity = timezone.now()
        self.save(update_fields=["last_activity"])

    class Meta:
        abstract = True
