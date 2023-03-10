"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from distutils.util import strtobool
from pathlib import Path
import os
import environ
import logging
from django.utils.log import DEFAULT_LOGGING

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR.parent, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-40o3*ui1nkjxf7yqz(wgk&22a3r)f!p14@bw99xx+afh@fnqvd"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = strtobool(os.getenv("DEBUG", "false"))

# https://docs.djangoproject.com/en/4.1/ref/settings/#std:setting-ALLOWED_HOSTS
allowed_hosts = os.getenv("ALLOWED_HOSTS", ".localhost,127.0.0.1,[::1]")
ALLOWED_HOSTS = list(map(str.strip, allowed_hosts.split(",")))
# ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = ["https://*.cycletourmap.com"]
ROOT_URL = os.getenv("ROOT_URL", "http://localhost:8000")

# Application definition

INSTALLED_APPS = [
    "apps.authentication",
    "apps.home",
    "apps.cycletourmap",
    "apps.strava",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "crispy_forms",
    "crispy_bootstrap5",
    "leaflet",
    "mathfilters",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "login"
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")  # ROOT dir for templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.context_processors.cfg_assets_root",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Extra places for collectstatic to find static files.
STATIC_URL = "static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = "/public_collected"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
ASSETS_ROOT = os.getenv("ASSETS_ROOT", "/static/assets")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Setting to use custom user model
AUTH_USER_MODEL = "authentication.Athlete"

# Strava details
STRAVA_CLIENTID = os.getenv("STRAVA_CLIENTID")
STRAVA_CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
STRAVA_VERIFY_TOKEN = os.getenv("STRAVA_VERIFY_TOKEN")
MAPBOX_ACCESS_TOKEN = os.getenv("MAPBOX_ACCESS_TOKEN")

# Crispy Forms Config
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGGING_CONFIG = None

LOGLEVEL = os.environ.get("DJANGO_LOG_LEVEL", "info").upper()

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                # exact format is not important, this is the minimum information
                "format": "[DJANGO] %(levelname)s %(asctime)s %(module)s %(name)s.%(funcName)s:%(lineno)s: %(message)s",
            },
            # "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
        },
        "handlers": {
            # console logs to stderr
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            # "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
        },
        "loggers": {
            # default for all undefined Python modules
            "": {
                "level": "INFO",
                "handlers": ["console"],
            },
            # Our application code
            "app": {
                "level": LOGLEVEL,
                "handlers": ["console"],
                # Avoid double logging because of root logger
                "propagate": False,
            },
            # Default runserver request logging
            # "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
        },
    }
)

LEAFLET_CONFIG = {
    "TILES": [
        (
            "Mapbox Streets",
            "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
            {
                "attribution": '?? <a href="https://www.mapbox.com/about/maps/">Mapbox</a> ?? <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
                "tileSize": 512,
                "maxZoom": 18,
                "zoomOffset": -1,
                "id": "mapbox/streets-v12",
                "accessToken": MAPBOX_ACCESS_TOKEN,
            },
        ),
        (
            "Mapbox Outdoors",
            "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
            {
                "attribution": '?? <a href="https://www.mapbox.com/about/maps/">Mapbox</a> ?? <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
                "tileSize": 512,
                "maxZoom": 18,
                "zoomOffset": -1,
                "id": "mapbox/outdoors-v12",
                "accessToken": MAPBOX_ACCESS_TOKEN,
            },
        ),
        (
            "OpenStreetMaps",
            "http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            {
                "attribution": '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            },
        ),
        (
            "OpenCycleMaps",
            "https://tile.thunderforest.com/cycle/{z}/{x}/{y}.png?apikey=3d3c357594e04c67a183d3c95a1792c0",
            {
                "attribution": '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            },
        ),
    ]
}
