from django.utils.translation import gettext_lazy as _

MAX_LENGTH_USERNAME = 30
USERNAME_HELP_TEXT = (
    f"Обязательное поле. {MAX_LENGTH_USERNAME} символов или меньше. Допустимые "
    "символы: буквы, цифры и @/./+/-/_"
)
USERNAME_ERROR_TEXT = _("A user with that username already exists.")
