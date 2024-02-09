import re

from django.core.validators import RegexValidator

from apps.general.constants import EMAIL_ERROR_TEXT, EMAIL_HELP_TEXT


class CustomEmailValidator(RegexValidator):
    regex = r"^[a-z0-9+_.-]{2,192}@[a-z0-9.-]{3,63}$"
    message = f"{EMAIL_ERROR_TEXT} {EMAIL_HELP_TEXT}"
    flags = re.IGNORECASE
