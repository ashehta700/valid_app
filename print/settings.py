"""
Django settings for print project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.core.files.storage import FileSystemStorage
import pathlib

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Define the UNC path to your shared folder
UNC_PATH = r'\\192.168.160.15'
MEDIA_ROOT = os.path.join(UNC_PATH, 'sharedIntegrationDocument')

os.makedirs(MEDIA_ROOT, exist_ok=True)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--!syc%#^oyqjz9ej6_@y@_a&%o12(z)qq-^bspk1vxea6@jc0%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'printPreview',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'print.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'print.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
 'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR, 'db.sqlite3'),
    },
   'ida': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'DEV',
            'USER': 'MSA',
            'PASSWORD': 'MSA',
            'HOST': '192.168.160.123',
            'PORT': '1521',
    },
    # 'sdi': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'newPortal',
    #     'USER' : 'postgres',
    #     'PASSWORD' : 'postgres',
    #     'HOST' : '10.100.100.71',
    #     'PORT' : '5432'
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH_USER_MODEL = 'accounts.User'
LOGIN_REQUIRED_URLS = (
        r'index',
    )
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# MEDIA_ROOT = r'//192.168.160.15/sharedIntegrationDocument/' # Directory where uploaded media is saved.
# MEDIA_URL = r'//192.168.160.15/sharedIntegrationDocument/' 




# # 0-------------0 for file upload in anthor place 
# FTP_USER = 'testuser'#os.environ['FTP_USER']
# FTP_PASS = 'testpassword'#os.environ['FTP_PASS']
# FTP_PORT = '21'#os.environ['FTP_PORT']
# DEFAULT_FILE_STORAGE = 'storages.backends.ftp.FTPStorage'
# FTP_STORAGE_LOCATION = 'ftp://' + FTP_USER + ':' + FTP_PASS + '@192.168.0.200:' + FTP_PORT
