# -*- coding: utf-8 -*-

from django.conf import settings


# Log anonimus actions?
ANONIMUS = getattr(settings, 'ACTIVITYLOG_ANONIMUS', True)

# Update last activity datetime in user profile
LAST_ACTIVITY = getattr(settings, 'ACTIVITYLOG_LAST_ACTIVITY', True)

# Only this methods will be logged
METHODS = getattr(settings, 'ACTIVITYLOG_METHODS',
                  ('GET', 'POST', 'PUT', 'PATCH', 'DELETE'))

# List of response statuses, which logged. By default - all logged.
# Don't use with ACTIVITYLOG_EXCLUDE_STATUSES
STATUSES = getattr(settings, 'ACTIVITYLOG_STATUSES', None)

# List of response statuses, which ignores. Don't use with ACTIVITYLOG_STATUSES
EXCLUDE_STATUSES = getattr(settings, 'ACTIVITYLOG_EXCLUDE_STATUSES', None)

# URL substrings, which ignores
EXCLUDE_URLS = getattr(settings, 'ACTIVITYLOG_EXCLUDE_URLS', ())
