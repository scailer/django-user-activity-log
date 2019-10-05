# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from . import models


class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'request_method', 'request_url',
                    'response_code', 'datetime', 'ip_address')
    list_filter = ('request_method', 'response_code')
    search_fields = ('user', 'request_url', '^ip_address')
    show_full_result_count = False


admin.site.register(models.ActivityLog, LogAdmin)
