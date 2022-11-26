import os
import dj_database_url
from .common import *

DEBUG = False


SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['tiger-prod.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}


CELERY_BROKER_URL = 'redis://localhost:6379/1'


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}