"""
Django settings for timeline project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import dotenv
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Add .env variables anywhere before SECRET_KEY

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = 'your_secret_key'
SECRET_KEY = os.environ['SECRET_KEY']  # Instead of your actual secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 3
# TODO Check reason-> https://medium.com/@pratique/social-login-with-react-and-django-i-c380fe8982e2
# TODO Encdure matching with data init

# TODO remove,  DEV ONLY
CORS_ALLOWED_ORIGINS = ['http://localhost:3000']
CORS_ALLOW_CREDENTIALS = True  # To allow JWT cookie (safer than WebStorage...)
CORS_EXPOSE_HEADERS = ['Access-Control-Allow-Credentials']
# CSRF_TRUSTED_ORIGINS = [    'change.allowed.com',] # TODO Need more work for comprehension/implementation
CSRF_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SECURE = True  # TODO Once https setup

# Application definition
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',

        # 'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


# JWT_ALLOW_REFRESH  = True #Todo -> Add refresh on each action or after "some" time
# -> https://jpadilla.github.io/django-rest-framework-jwt/#refresh-token

REST_USE_JWT = True
# Use cookies rather than WebStorage to reduce security issues (with addition of CSRF protection)
JWT_AUTH_COOKIE = 'jwt-auth'
# JWT_AUTH_SECURE = False  # Allow Https only TODO
# JWT_AUTH_COOKIE_USE_CSRF # TODO Use it?
# JWT_AUTH_COOKIE_ENFORCE_CSRF_ON_UNAUTHENTICATED # TODO Use?

REST_AUTH_SERIALIZERS = {
    # serializer in dj_rest_auth.views.LoginView
    'LOGIN_SERIALIZER': 'dj_rest_auth.serializers.LoginSerializer',
    # response for successful authentication in dj_rest_auth.views.LoginView
    'JWT_SERIALIZER': 'dj_rest_auth.serializers.JWTSerializer',
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django rest framework
    'rest_framework',
    'rest_framework.authtoken',  # For django REST / Django token authent
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'drf_yasg',
    'corsheaders',  # TODO remove, DEV ONLY

    # TODO add knox to encode clientID and

    # for social login
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'api'
]

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    #    'django.contrib.auth.backends.ModelBackend',
)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # TODO remove, DEV ONLY
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'timeline.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'timeline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
