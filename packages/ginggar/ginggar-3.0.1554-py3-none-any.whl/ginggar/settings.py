# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Default Django settings for Ginggar.

If you find this file in a Ginggar installation (instead of the developer's source code), be aware of the fact that this
file contains the factory default. Overriding values is possible by writing them to a :file:`settings_local.py` file.
"""


DEBUG = True

MANAGERS = ADMINS = []

SECRET_KEY = "c628b1b3c0bdf2a3d14dbfcba1444f41"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/tmp/ginggar-db",
        "USER": "ingwer",
        "PASSWORD": "ingwer",
    }
}

TIME_ZONE = "UTC"

LANGUAGE_CODE = "en-us"

STATIC_ROOT = "/var/lib/ginggar/static/"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ginggar.urls"

TEMPLATES = [
{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
    "APP_DIRS": True,
    "OPTIONS": {
        "context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ],
        "debug": DEBUG,
    },
},]

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "ginggar.main",
)

SUB_SITE = "/"

ALLOWED_HOSTS = ["*"]

# search for EXTERNAL_AUTH_HELPER in Ginggar manual
EXTERNAL_AUTH_HELPER = None

# search for SINGLE_USER_MODE in Ginggar manual
SINGLE_USER_MODE = False

try:
    from .settings_local import *
except ImportError:
    pass

LOGIN_URL = f"{SUB_SITE}login/"
STATIC_URL = f"{SUB_SITE}static/"
