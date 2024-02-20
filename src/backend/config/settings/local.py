from .base import *  # noqa

DEBUG = getenv("DEBUG", default="False") == "True"

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
            "NAME": getenv("DB_NAME", default="test"),
            "USER": getenv("POSTGRES_USER", default="test_user"),
            "PASSWORD": getenv("POSTGRES_PASSWORD", default="test_password"),
            "HOST": getenv("DB_HOST", default="db"),
            "PORT": getenv("DB_PORT", default=5432),
        }
    }

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
