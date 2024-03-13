from .base import *
ALLOWED_HOSTS = ['localhost']
DEBUG = True
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'local_db',
'HOST': '127.0.0.1',
'PORT': '5432',
}
}

SECRET_KEY = os.environ['SECRET_KEY']