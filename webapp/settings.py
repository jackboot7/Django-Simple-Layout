# 
# Django settings for a simple django project.
#

#==============================
# Calculation of paths.
#==============================

import os

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR = os.path.split(SITE_ROOT)[0]

VAR_ROOT = os.path.join(PROJECT_DIR, 'var')
if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#==============================
# Production database config.
#==============================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'project_database', 
        'USER': 'database_user', 
        'PASSWORD': 'database_password', 
        'HOST': 'localhost', 
        'PORT': '', 
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'en-us'
SITE_ID = 1


#===============================
# URLs and media settings.
#===============================

ROOT_URLCONF = 'urls'

MEDIA_URL = '/uploads'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'j_flbhep6uh9j%e10mw6%2*(@notj2n&p-mf(-scg6edsgvsvr'

#========================================
# Templates
#========================================

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

#=================================
# Middleware
#=================================

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

#=================================
# Applications
#=================================
#
# All the settings for installed aplications must be in this section
#

INSTALLED_APPS = (
    # Django apps.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps.
    # 'djcelery',
    
    # Project apps. 
    # Anything living in the apps dir.
)

#==========================
# Login std. settings.
#==========================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#=======================
# Import local settings
#=======================

try:
    from local_settings import *
except ImportError:
    pass

