"""
Django settings for birdo project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

For the configurations module and it's values, see
https://github.com/jezdez/django-configurations
"""

from os.path import dirname, abspath

from configurations import Configuration, values


BASE_DIR = dirname(dirname(abspath(__file__)))


class Common(Configuration):

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'vhmc9lo887c)w%dum0oln(!wof(m#+f5$j8p#%&v=(3946n2ht'

    # SECURITY WARNING: don't run with debug turned on in production!
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG

    ALLOWED_HOSTS = []

    # APP CONFIGURATION
    DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.gis',
    )

    # Third-party apps, patches, fixes
    THIRD_PARTY_APPS = (
        'mptt',
        'django_mptt_admin',
        'django_extensions',
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        'birds',
        'shares',
    )

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    ROOT_URLCONF = 'birdo.urls'

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

    WSGI_APPLICATION = 'birdo.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
    # https://github.com/kennethreitz/dj-database-url

    DATABASES = values.DatabaseURLValue('postgis://birdo_user@localhost/birdo')

    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATIC_URL = '/static/'

    # Social Network settings

    TWITTER_KEY = values.SecretValue()
    TWITTER_SECRET = values.SecretValue()
