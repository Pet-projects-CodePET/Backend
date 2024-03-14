import re
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = getenv("SECRET_KEY")


ALLOWED_HOSTS = list(
    str(getenv("ALLOWED_HOSTS", default=["localhost,127.0.0.1"])).split(",")
)


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "django_filters",
    "drf_spectacular",
]

LOCAL_APPS: list = [
    "apps.general",
    "apps.users",
    "apps.projects",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

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

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            Path(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": getenv("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": getenv("POSTGRES_DB", default="db_test"),
        "USER": getenv("POSTGRES_USER", default="admin_test"),
        "PASSWORD": getenv("POSTGRES_PASSWORD", default="postgre_admin"),
        "HOST": getenv("POSTGRES_HOST", default="db_test"),
        "PORT": getenv("POSTGRES_PORT", default=5432),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "apps.users.validators.PasswordMaximumLengthValidator",
        "OPTIONS": {
            "message": "Пароль слишком длинный.",
        },
    },
    {
        "NAME": "apps.users.validators.PasswordRegexValidator",
        "OPTIONS": {
            "message": "В пароле недопустимые символы.",
            "help_message": "В пароле допускаются цифры, буквы и спецсимовлы -!#$%%&'*+/=?^_;():@,.<>`{}~«»",
            "regex": r"(^[-%!#$&*'+/=?^_;():@,.<>`{|}~-«»0-9A-ZА-ЯЁ]+)\Z",
            "flags": re.IGNORECASE,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATIC_ROOT = Path(BASE_DIR, "static")

MEDIA_URL = "media/"
MEDIA_ROOT = Path(BASE_DIR, "media")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "HIDE_USERS": False,
    "PERMISSIONS": {
        "user_list": ["rest_framework.permissions.IsAuthenticated"],
    },
    "USER_CREATE_PASSWORD_RETYPE": True,
    "AUTO_ACTIVATE_NEW_USERS": True,
    "SERIALIZERS": {
        "current_user": "api.v1.users.serializers.CustomUserSerializer",
        "user": "api.v1.users.serializers.CustomUserSerializer",
        "user_create_password_retype": "api.v1.users.serializers.CustomUserCreateSerializer",
    },
    "SEND_ACTIVATION_EMAIL": False,
    "SEND_CONFIRMATION_EMAIL": True,
    "ACTIVATION_URL": "#/login/{token}",
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
    "EMAIL": {
        "confirmation": "api.v1.users.emails.RegistrationConfirmEmail",
        "password_reset": "api.v1.users.emails.PasswordResetEmail",
    },
}

EMAIL_HOST = getenv("EMAIL_HOST", default="localhost")
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD", default="")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


SPECTACULAR_SETTINGS = {
    "TITLE": "CodePET",
    "DESCRIPTION": "CodePET - это веб-приложение, разработанное для поиска, организации и управления пет-проектами в "
    "области разработки программного обеспечения. Оно предназначено для выпускников школ "
    "программирования, которые хотят получить практический опыт и совершенствовать свои навыки путем "
    "участия в реальных проектах. А также оно будет интересно для опытных разработчиков которые хотят "
    "реализовать что-то новое, для менеджеров проектов и для компаний которые хотят создать тестовое "
    "МВП нового продукта.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "filter": True,
    },
    "COMPONENT_SPLIT_REQUEST": True,
}
