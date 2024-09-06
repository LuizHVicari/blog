import os
from pathlib import Path
from django.utils.translation import gettext_lazy
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY', cast=str)

DEBUG = config('DJANGO_DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=str).split(' ')

CSRF_TRUSTED_ORIGINS = config('DJANGO_CSRF_TRUSTED_ORIGINS', cast=str).split(' ')

SECURE_HSTS_SECONDS=config('DJANGO_SECURE_HSTS_SECONDS', cast=bool, default=True)
SECURE_SSL_REDIRECT=config('DJANGO_SECURE_SSL_REDIRECT', cast=bool, default=True)
SESSION_COOKIE_SECURE = config('DJANGO_SESSION_COOKIE_SECURE', cast=bool, default=True)
CSRF_COOKIE_SECURE = config('DJANGO_CSRF_COOKIE_SECURE', cast=bool, default=True)
SECURE_HSTS_PRELOAD = config('DJANGO_SECURE_HSTS_PRELOAD', cast=bool, default=str)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'rosetta',
    'parler',

    # custom
    'apps.core',
    'apps.posts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            (BASE_DIR / 'templates/')
        ],
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

TEMPLATES_DIRS = [
    os.path.join(BASE_DIR, 'templates/')
]

WSGI_APPLICATION = 'blog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PG_DB'),
        "USER": config("PG_USER"),
        "PASSWORD": config("PG_PASSWORD"),
        "HOST": config("PG_HOST"),
        "PORT": config("PG_PORT", cast=str, default='5432'),
    }
}

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

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en', 'English'),
    ('pt', 'Portuguese')
]
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PARLER_DEFAULT_LANGUAGE_CODE = 'en-us'

PARLER_LANGUAGES = {
    None: (
        {'code': 'en',},
        {'code': 'pt',},
    ),
    'default': {
        'fallbacks': ['en'],      
        'hide_untranslated': False, 
    }
}

ROSETTA_LOGIN_URL = '/admin/login'