This django app intended for writing HTTP log to database and/or watch last user activity.

Features:
- DB router for writing logs to another database.
- Filters for ignoring some queries by URL, HTTP methods and response codes.
- Saving anonymous activity as fake user.
- Autocreation log DB (for postgresql)

Install:

$ pip install django-user-activity-log2

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

DATABASE_ROUTERS = ['activity_log.router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {'activity_log': 'logs'}

# If you set up DATABASE_APPS_MAPPING, but don't set related value in
# DATABASES, it will created automatically using "default" DB settings
# as example.
DATABASES = {
    'logs': {
        ...
    },
}

# Create DB automatically (for postgres, and may be mysql).
# We create log database automatically using raw SQL in pre_migrate signal.
# You must insure, that DB user has permissions for creation databases. 
# Tested only for postgresql
ACTIVITYLOG_AUTOCREATE_DB = False

# App settings

# Log anonymous actions?
ACTIVITYLOG_ANONYMOUS = True

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

If you use ACTIVITYLOG_AUTOCREATE_DB migrations to logs database 
will be run automatically.
