from .base import *  # noqa

DEBUG = False


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_PORT = 465
