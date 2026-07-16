"""
Django settings for clinic project.
"""

from pathlib import Path
from decouple import config
import dj_database_url

# WhiteNoise: use non-manifest storage in production to avoid 500s when a static file
# is missing from the manifest during deploy.
# This prevents errors like:
# "Missing staticfiles manifest entry for 'img/logo.png'".



BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# Security
# =========================

SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-change-this-in-production"
)

DEBUG = config(
    "DEBUG",
    default=False,
    cast=bool
)


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "svdc-9ga4.onrender.com",
]


# =========================
# Production Security
# =========================

if not DEBUG:

    SECURE_SSL_REDIRECT = config(
        "SECURE_SSL_REDIRECT",
        default=True,
        cast=bool
    )

    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https"
    )

    USE_X_FORWARDED_HOST = True

    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = "DENY"


# =========================
# Applications
# =========================

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",

    "django.contrib.staticfiles",

    "whitenoise.runserver_nostatic",

    "sslserver",

    "home",
]


# =========================
# Middleware
# =========================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "clinic.urls"


# =========================
# Templates
# =========================

TEMPLATES = [

    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],
        },
    },
]


WSGI_APPLICATION = "clinic.wsgi.application"


# =========================
# Database
# =========================

DATABASES = {

    "default": dj_database_url.config(

        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",

        conn_max_age=600,

        conn_health_checks=True,
    )
}



# =========================
# Password Validation
# =========================

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# =========================
# Internationalization
# =========================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



# =========================
# Static Files
# =========================

STATIC_URL = "/static/"


# Source static folder
STATICFILES_DIRS = [

    BASE_DIR / "static",

]


# Collected static folder
STATIC_ROOT = BASE_DIR / "staticfiles"



# Django 5.2 + WhiteNoise
STORAGES = {

    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },

}



# =========================
# Default Primary Key
# =========================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)



# =========================
# Email
# =========================

if DEBUG:

    EMAIL_BACKEND = (
        "django.core.mail.backends.console.EmailBackend"
    )

else:

    EMAIL_BACKEND = (
        "django.core.mail.backends.smtp.EmailBackend"
    )

    EMAIL_HOST = config(
        "EMAIL_HOST",
        default="smtp.gmail.com"
    )

    EMAIL_PORT = config(
        "EMAIL_PORT",
        default=587,
        cast=int
    )

    EMAIL_USE_TLS = True

    EMAIL_HOST_USER = config(
        "EMAIL_HOST_USER",
        default=""
    )

    EMAIL_HOST_PASSWORD = config(
        "EMAIL_HOST_PASSWORD",
        default=""
    )


DEFAULT_FROM_EMAIL = config(
    "EMAIL_HOST_USER",
    default="webmaster@localhost"
)



# =========================
# Logging
# =========================

LOGGING = {

    "version": 1,

    "disable_existing_loggers": False,

    "handlers": {

        "console": {

            "class":
            "logging.StreamHandler",

        },

    },

    "root": {

        "handlers":
        [
            "console"
        ],

        "level":
        "INFO",

    },

}