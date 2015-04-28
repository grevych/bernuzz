# -*- coding:utf-8 -*-

import os

from private import *



BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print BASE_DIR


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    #'social.apps.django_app.me',
    'basic',
    'hierarchy',
    'workflow',
    'management',
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
MEDIA_URL = '/media/'

#STATIC_ROOT = 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),

)

print os.path.join(BASE_DIR, 'static')


AUTHENTICATION_BACKENDS = (
    #'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenIdConnect',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',
    'social.backends.google.GooglePlusAuth',


    #For username/password login
    'django.contrib.auth.backends.ModelBackend',
)



TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.contrib.messages.context_processors.messages',

)

TEMPLATE_DIRS = (
    'templates/',
)

# backends: context processor will load a backends key in the context with three entries on it:
# associated: It’s a list of UserSocialAuth instances related with the currently logged in user. Will be empty if there’s no current user.
# not_associated: A list of available backend names not associated with the current user yet. If there’s no user logged in, it will be a list of all available backends.
# backends: A list of all available backend names.


#SOCIAL_AUTH_USER_MODEL = 'django.contrib.auth.models.User'

#SOCIAL_AUTH_STORAGE = 'social.apps.django_app.me.models.DjangoStorage'


SOCIAL_AUTH_URL_NAMESPACE = 'social'

#Used to redirect the user once the auth process ended successfully. The value of ?next=/foo is used if it was present '/logged-in/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

#URL where the user will be redirected in case of an error '/login-error/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'

#Is used as a fallback for LOGIN_ERROR_URL '/login-url/'
SOCIAL_AUTH_LOGIN_URL = '/'

#Used to redirect new registered users, will be used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL if defined.
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'

#Like SOCIAL_AUTH_NEW_USER_REDIRECT_URL but for new associated accounts (user is already logged in). Used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'

#The user will be redirected to this URL when a social account is disconnected
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'

#Inactive users can be redirected to this URL when trying to authenticate.
SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'



SOCIAL_AUTH_SANITIZE_REDIRECTS = True

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

SOCIAL_AUTH_SESSION_EXPIRATION = False

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']



SOCIAL_AUTH_GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = False
SOCIAL_AUTH_GOOGLE_PLUS_AUTH_EXTRA_ARGUMENTS = {
      'access_type': 'offline'
}
