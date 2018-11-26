import dj_database_url

from .base import *


DEBUG = False

ALLOWED_HOSTS = ["REDACTED"]

DATABASES = {"default": dj_database_url.config(conn_max_age=600)}


##########


PERMANENT_REDIRECT = True
