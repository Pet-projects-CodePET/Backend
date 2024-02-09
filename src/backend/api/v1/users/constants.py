from django.contrib.auth import get_user_model
from djoser.conf import settings as djoser_settings

ORDERED_USERS_FIELDS = (
    djoser_settings.USER_ID_FIELD,
    djoser_settings.LOGIN_FIELD,
) + tuple(get_user_model().REQUIRED_FIELDS)
