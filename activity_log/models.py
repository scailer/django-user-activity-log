# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class ActivityLog(models.Model):
    user_id = models.IntegerField(_('user id '))
    user = models.CharField(_('user'), max_length=256)
    request_url = models.CharField(_('url'), max_length=256)
    request_method = models.CharField(_('http method'), max_length=10)
    response_code = models.CharField(_('response code'), max_length=3)
    datetime = models.DateTimeField(_('datetime'), default=timezone.now)

    class Meta:
        verbose_name = _('activity log')


class UserMixin(models.Model):
    last_activity = models.DateTimeField(
        _('last activity'), default=timezone.now)

    def update_last_activity(self):
        self.last_activity = timezone.now()
        self.save()

    class Meta:
        abstract = True
