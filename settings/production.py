import django_heroku
import dj_database_url 
import settings.common


DEBUG = False

ALLOWED_HOSTS = []

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES = {}
DATABASES['default'].update(prod_db)

django_heroku.settings(locals())