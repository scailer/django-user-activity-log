# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.module_loading import import_string as _load
from .models import ActivityLog
from . import conf


def get_ip_address(request):
    for header in conf.IP_ADDRESS_HEADERS:
        addr = request.META.get(header)
        if addr:
            return addr.split(',')[0].strip()


def get_extra_data(request, response):
    if not conf.GET_EXTRA_DATA:
        return
    return _load(conf.GET_EXTRA_DATA)(request, response)


class ActivityLogMiddleware:
    def process_request(self, request):
        if conf.LAST_ACTIVITY and request.user.is_authenticated():
            getattr(request.user, 'update_last_activity', lambda: 1)()

    def process_response(self, request, response):
        miss_log = [
            not(conf.ANONIMOUS or request.user.is_authenticated()),
            request.method not in conf.METHODS,
            any(url in request.path for url in conf.EXCLUDE_URLS)
        ]

        if conf.STATUSES:
            miss_log.append(response.status_code not in conf.STATUSES)

        if conf.EXCLUDE_STATUSES:
            miss_log.append(response.status_code in conf.EXCLUDE_STATUSES)

        if any(miss_log):
            return response

        if request.user.is_authenticated():
            user, user_id = request.user.get_username(), request.user.pk
        else:
            user, user_id = 'anon_{}'.format(request.session.session_key), 0

        ActivityLog.objects.create(
            user_id=user_id,
            user=user,
            request_url=request.build_absolute_uri()[:255],
            request_method=request.method,
            response_code=response.status_code,
            ip_address=get_ip_address(request),
            extra_data=get_extra_data(request, response)
        )

        return response
