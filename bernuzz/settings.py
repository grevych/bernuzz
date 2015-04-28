# -*- coding:utf-8 -*-
"""
Django settings for bernuzz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3s_rm_^x*=g(k*!()*$ls*6hn5jm8&7l8l9ck5v(owt@hzfo-y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'basic',
    'hierarchy',
    'management',
    'workflow',
    'social.apps.django_app.default',
    #'social.apps.django_app.me',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bernuzz.urls'

WSGI_APPLICATION = 'bernuzz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bernuzz',
        'USER': 'bernuzz',
        'PASSWORD': 'devel',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',

    #For username/password login
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

# backends: context processor will load a backends key in the context with three entries on it:
# associated: It’s a list of UserSocialAuth instances related with the currently logged in user. Will be empty if there’s no current user.
# not_associated: A list of available backend names not associated with the current user yet. If there’s no user logged in, it will be a list of all available backends.
# backends: A list of all available backend names.


SOCIAL_AUTH_USER_MODEL = 'foo.bar.User'

#SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'


SOCIAL_AUTH_URL_NAMESPACE = 'social'

#Used to redirect the user once the auth process ended successfully. The value of ?next=/foo is used if it was present
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'

#URL where the user will be redirected in case of an error
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'

#Is used as a fallback for LOGIN_ERROR_URL
SOCIAL_AUTH_LOGIN_URL = '/login-url/'

#Used to redirect new registered users, will be used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL if defined.
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'

#Like SOCIAL_AUTH_NEW_USER_REDIRECT_URL but for new associated accounts (user is already logged in). Used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'

#The user will be redirected to this URL when a social account is disconnected
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'

#Inactive users can be redirected to this URL when trying to authenticate.
SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'

SOCIAL_AUTH_SANITIZE_REDIRECTS = True

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

SOCIAL_AUTH_SESSION_EXPIRATION = False

