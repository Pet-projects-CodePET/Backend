from django.utils.translation import gettext_lazy as _

MAX_LENGTH_USERNAME = 30
MIN_LENGTH_USERNAME = 2
USERNAME_REGEX = r"^[A-Za-zА-Яа-я0-9_.-]+\Z"
USERNAME_ERROR_REGEX_TEXT = (
    "Допустимые символы: кирилические или латинсикие буквы, цифры и /./-/_"
)
USERNAME_HELP_TEXT = (
    f"Обязательное поле. От {MIN_LENGTH_USERNAME} до {MAX_LENGTH_USERNAME} "
    f" символов. {USERNAME_ERROR_REGEX_TEXT}"
)
USERNAME_ERROR_TEXT = _("A user with that username already exists.")
