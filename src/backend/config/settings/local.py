from .base import *  # noqa

DEBUG = getenv("DEBUG", default="True") == "True"

if getenv("USE_SQLITE", default="True") == "True":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": str(BASE_DIR / "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": getenv(
                "DB_ENGINE", default="django.db.backends.postgresql"
            ),
            "NAME": getenv("POSTGRES_DB", default="db_test"),
            "USER": getenv("POSTGRES_USER", default="admin_test"),
            "PASSWORD": getenv("POSTGRES_PASSWORD", default="postgre_admin"),
            "HOST": getenv("POSTGRES_HOST", default="db_test"),
            "PORT": getenv("POSTGRES_PORT", default=5432),
        }
    }

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "level": "INFO",
            "handlers": [
                "console",
            ],
        },
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": [
                "console",
            ],
            "propagate": False,
        },
    },
}


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
