from .base import *
import dj_database_url
import os

URL_POSTGRES = os.getenv("DATABASE_URL")
ALLOWED_HOSTS = [ 'localhost', '*.herokuapp.com', 'dev-final-project-info.herokuapp.com', ]



# DATABASES['default'] = dj_database_url.config(conn_max_age=600)

DATABASES['default'] = dj_database_url.parse(URL_POSTGRES, conn_max_age=600)

