# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from activity_log.models import UserMixin


class User(AbstractUser, UserMixin):
    class Meta:
        verbose_name = 'user'
