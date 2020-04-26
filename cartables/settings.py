"""
Django settings for cartables project.

Generated by 'django-admin startproject' using Django 1.10.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

# -*- coding: utf8 -*-

import os
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '92+a$08_84ac&*n4xvt&cup&%ymq2=etk#df_l(w0b6t&!n2c)'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('ENV') == 'PRODUCTION':
    DEBUG = False
else:
    DEBUG = True


ALLOWED_HOSTS = ['localhost','127.0.0.1','cartablesdafrique.com','https://www.cartablesdafrique.com','www.cartablesdafrique.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'parrainage',
    'acceuil',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cartables.urls'

TEMPLATES = [
    {
       'BACKEND': 'django.template.backends.django.DjangoTemplates',
# VERSION CLEMENT
#        'DIRS': ['/Users/clem/Documents/GitHub/my-first-blog/templates/',''],
# VERSION LIONEL
#        'DIRS': ['',''],
# VERSION ROLAND
#        'DIRS': ['/Users/roland/Projets/templates/',''],
# VERSION VICTOR
        'DIRS': ['/Users/jvtraore/GitHub/my-first-blog/templates/',''],
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

WSGI_APPLICATION = 'cartables.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
#        'OPTIONS': {"init_command": "SET foreign_key_checks = 0;"},
# VERSION CLEMENT
#        'NAME': 'site_cartables',
#        'USER': 'root',
#        'PASSWORD': 'apple123',
# VERSION LIONEL
#        'NAME': '',
#        'USER': '',
#        'PASSWORD': '',
# VERSION ROLAND
#        'NAME': 'site_cartables',
#        'USER': 'root',
#        'PASSWORD': 'NataSQL$',
# VERSION VICTOR
        'NAME': 'sitecartable',
        'USER': 'root',
        'PASSWORD': 'ewenvictor',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/Users/roland/Projets/static/'

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# This one was not by default and has been added for this project

#STATICFILES_DIRS = (
#                    )
#
#if os.environ.get('ENV') == 'PRODUCTION':

    # Static files settings
#    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

#
    # Extra places for collectstatic to find static files.
#        os.path.join(PROJECT_ROOT, 'static'),
#    )

STATICFILES_DIRS = (
#   VERSION CLEMENT
#                    "/Users/clem/Documents/GitHub/my-first-blog/static/",
# VERSION LIONEL
#                    "Lionel met ton chemin ici stp pour acceder a ton dossier static",
#   VERSION ROLAND
#                    "/Users/roland/Projets/static/",
#   VERSION VICTOR
                    "/Users/jvtraore/GitHub/my-first-blog/static/",
                    )

# Complete automatically URL with slash
APPEND_SLASH = True

