# -*- coding: utf-8 -*-

from . import conf
from .models import ActivityLog


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
            request_url=request.build_absolute_uri(),
            request_method=request.method,
            response_code=response.status_code
        )

        return response
