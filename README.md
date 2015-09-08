This django app intended for writing HTTP log to database and/or watch last user activity.

Features:
- DB router for writing logs to another database.
- Filters for ignoring some queries by URL, HTTP methods and response codes.
- Saving anonymous activity as fake user.

Install:

$ pip install django-user-activity-log

settings.py:


```python
INSTALLED_APPS = (
    ...
    'activity_log',
)

MIDDLEWARE_CLASSES = (
    ...
    'activity_log.middleware.ActivityLogMiddleware',
)

# For writing log to another DB
DATABASES = {
    'logs': {
        ...
    },
}

DATABASE_ROUTERS = ['activity_log.router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {'activity_log': 'logs'}

# App settings

# Log anonimus actions?
ACTIVITYLOG_ANONIMOUS = True

# Update last activity datetime in user profile. Needs updates for user model.
ACTIVITYLOG_LAST_ACTIVITY = True

# Only this methods will be logged
ACTIVITYLOG_METHODS = ('POST', 'GET')

# List of response statuses, which logged. By default - all logged.
# Don't use with ACTIVITYLOG_EXCLUDE_STATUSES
ACTIVITYLOG_STATUSES = (200, )

# List of response statuses, which ignores. Don't use with ACTIVITYLOG_STATUSES
# ACTIVITYLOG_EXCLUDE_STATUSES = (302, )

# URL substrings, which ignores
ACTIVITYLOG_EXCLUDE_URLS = ('/admin/activity_log/activitylog', )
```

account/models.py:

```python
from django.contrib.auth.models import AbstractUser
from activity_log.models import UserMixin

# Only for LAST_ACTIVITY = True
class User(AbstractUser, UserMixin):
    pass
```

$ python manage.py migrate & python manage.py migrate --database=logs
