"""
Django settings for diversityFIRST project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku, dj_database_url
from decouple import config



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['herokuapp.com', '127.0.0.1', 'diversity-first.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'home',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'easy_pdf',
    'storages',

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'diversityFIRST.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'diversityFIRST.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': config('db_password'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#URL = the url, root = where we want to put them -> 1st = rootm 2nd arg = own path


#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#MEDIA_URL ='/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'home/media')

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_DIRS = [
#    ('node_modules', os.path.join(BASE_DIR, 'node_modules')),
#]

#angluar stuff
#FORM_RENDERER = 'djng.forms.renderers.DjangoAngularTemplates'


#heroku stuff
import dj_database_url
db_from_env = dj_database_url.config('postgres://postgres:{}@localhost:5432/postgres'.format(config('db_password')))
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500
# Activate Django-Heroku.
django_heroku.settings(locals())


#static stuff

#AWS
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'home/static'),
]
AWS_ACCESS_KEY_ID = 'AKIAJTYSZXRLP6M46BRQ'
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'diversity-first-assets'

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'diversityFIRST.storage_backends.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'diversityFIRST.storage_backends.PublicMediaStorage'

AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'diversityFIRST.storage_backends.PrivateMediaStorage'
