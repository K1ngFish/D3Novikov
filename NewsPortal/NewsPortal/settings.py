"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4i19$3zj9!$yv2%dk6b)sv8!*#z8gzh5fta&!+ene*ru)lvmn+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    
    'django.contrib.sites',
    'django.contrib.flatpages',

    'NewsApp.apps.NewsAppConfig',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'subscriptions',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static']

LOGIN_REDIRECT_URL = '/posts'
LOGOUT_REDIRECT_URL = '/posts'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "dev3np0rt"
EMAIL_HOST_PASSWORD = "hzitzggynezfbnxm"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "dev3np0rt@yandex.ru"

SITE_URL = 'http://127.0.0.1:8000'

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://default:kc2hNDiYppdAeutRoYpXylitDAfPTuff@redis-14329.c300.eu-central-1-1.ec2.cloud.redislabs.com:14329'
CELERY_RESULT_BACKEND = 'redis://default:kc2hNDiYppdAeutRoYpXylitDAfPTuff@redis-14329.c300.eu-central-1-1.ec2.cloud.redislabs.com:14329'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# для django debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

ADMINS = [('admin', 'dev3np0rt@yandex.ru')]

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'loggers': {
		'django': {
		'handlers': ['console', 'general', 'errors', 'security', 'mail_admins'],
		'level': 'DEBUG',
		'propagate': True,
		},
		'django.request': {
        'handlers': ['errors', 'mail_admins'],
        'level': 'ERROR',
        'propagate': False,
        },
        'django.server': {
        'handlers': ['errors', 'mail_admins'],
        'level': 'ERROR',
        'propagate': False,
        },
        'django.template': {
        'handlers': ['errors'],
        'level': 'ERROR',
        'propagate': False,
        },
        'django.db.backends': {
        'handlers': ['errors'],
        'level': 'ERROR',
        'propagate': False,
		},
		'django.security': {
		'handlers': ['security', 'mail_admins'],
		'level': 'ERROR',
		'propagate': False
		},

	},
	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
			'level':'DEBUG',
			'formatter': 'standard',
			'filters': ['debug_true']
			},
		'warnings': {
			'class': 'logging.StreamHandler',
			'level': 'WARNING',
			'formatter': 'with_pathname',
			'filters': ['debug_true']
			},
		'errors_console': {
			'class': 'logging.StreamHandler',
			'level': 'ERROR',
			'formatter': 'with_excinfo',
			'filters': ['debug_true']
			},
		'general': {
		    'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'general.log',
            'level': 'INFO',
            'formatter': 'standard',
            'filters': ['debug_false']
			},
		'errors': {
		    'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'errors.log',
            'level': 'ERROR',
            'formatter': 'with_excinfo',
            'filters': ['debug_true']
			},
		'security': {
		    'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'security.log',
            'level': 'INFO',
            'formatter': 'security',
            'filters': ['debug_true']
			},
		'mail_admins': {
        	'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'include_html': True,
        },
	},
	'formatters': {
		'standard': {
			'format': '{asctime} {levelname} {message}',
			'datefmt': '%Y.%m.%d %H.%M.%S',
			'style': '{',
		},
		'with_pathname': {
			'format': '{asctime} {levelname} {message} {pathname}',
			'datefmt': '%Y.%m.%d %H.%M.%S',
			'style': '{',
		},
		'with_excinfo': {
			'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
			'datefmt': '%Y.%m.%d %H.%M.%S',
			'style': '{',
		},
		'security': {
			'format': '{asctime} {levelname} {name} {message}',
			'datefmt': '%Y.%m.%d %H.%M.%S',
			'style': '{',
		},
	},
	'filters': {
		'debug_true': {
			'()':'django.utils.log.RequireDebugTrue',
		},
		'debug_false': {
			'()':'django.utils.log.RequireDebugFalse',
		}
	}
}

