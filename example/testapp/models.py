# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from activity_log.models import UserMixin


class User(AbstractUser, UserMixin):
    class Meta:
        verbose_name = 'user'


def make_extra_data(request, response, body):
    return str(request.META)
