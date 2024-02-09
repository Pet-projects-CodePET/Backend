from django.utils.translation import gettext_lazy as _

MAX_LENGTH_NICKNAME = 30
NICKNAME_HELP_TEXT = _(
    "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ " "only."
)
NICKNAME_ERROR_TEXT = _("A user with that username already exists.")
