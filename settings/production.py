from settings.common import *
import django_heroku
import dj_database_url 


DEBUG = False

ALLOWED_HOSTS = ['bank-search-api.herokuapp.com']

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES = {}
DATABASES['default'] = {}
DATABASES['default'].update(prod_db)

django_heroku.settings(locals())