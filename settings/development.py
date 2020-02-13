import settings.common


DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = '6(j*ws^6!v3=b*v1h%81rk348!he2qyw3xgfteef(pa9hkrb2+'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'django',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}