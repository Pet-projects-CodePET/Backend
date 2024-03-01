from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from django.utils.translation import gettext_lazy as _
from PIL import Image

from apps.profile.constants import (
    ABOUT_ERROR_MESSAGE,
    MAX_LEN_ABOUT,
    MAX_LEN_NICKNAME,
    MAX_LEN_PORTFOLIO,
    MIN_LEN,
    MIN_LEN_ABOUT,
    MIN_LEN_PORTFOLIO,
    NICKNAME_ERROR_MESSAGE,
    PHONE_ERROR_MESSAGE,
    TEXT_ERROR_MESSAGE,
)


def validate_nickname(value):
    nickname_min_length = MinLengthValidator(
        MIN_LEN,
        message=NICKNAME_ERROR_MESSAGE,
    )
    nickname_max_length = MaxLengthValidator(
        MAX_LEN_NICKNAME,
        message=NICKNAME_ERROR_MESSAGE,
    )
    regex_validator = RegexValidator(
        regex=r"^[a-zA-Z\а-яА-ЯёЁ\d\s\-\.\,\&\+\№\!\_]+$",
        message=TEXT_ERROR_MESSAGE,
    )
    regex_validator(value)
    nickname_min_length(value)
    nickname_max_length(value)


def validate_about(value):
    about_min_length = MinLengthValidator(
        MIN_LEN_ABOUT,
        message=ABOUT_ERROR_MESSAGE,
    )
    about_max_length = MaxLengthValidator(
        MAX_LEN_ABOUT,
        message=ABOUT_ERROR_MESSAGE,
    )
    regex_validator = RegexValidator(
        regex=r"^[а-яА-ЯёЁ\-]+$",
        message=TEXT_ERROR_MESSAGE,
    )
    regex_validator(value)
    about_min_length(value)
    about_max_length(value)


def validate_portfolio(value):
    portfolio_min_length = MinLengthValidator(
        MIN_LEN_PORTFOLIO,
        message=ABOUT_ERROR_MESSAGE,
    )
    portfolio_max_length = MaxLengthValidator(
        MAX_LEN_PORTFOLIO,
        message=ABOUT_ERROR_MESSAGE,
    )
    # regex_validator = RegexValidator(regex=r'^[a-zA-Z\d]+$', message=TEXT_ERROR_MESSAGE, )


def validate_phone_number(value):
    regex_validator = RegexValidator(
        regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
        message=PHONE_ERROR_MESSAGE,
    )


def validate_image_format(value):
    valid_extensions = [".png", ".jpg", ".jpeg"]
    ext = value.name.lower().split(".")[-1]
    if not ext in valid_extensions:
        raise ValidationError(
            _("Пожалуйста загрузите файл с расширением PNG или JPEG.")
        )


def validate_image_size(value):
    max_size = 10 * 1024 * 1024  # 10 MB
    if value.size > max_size:
        raise ValidationError(_("Файл не должен превышать размер 10 MB."))


def validate_image_resolution(value):
    min_width, min_height = 320, 240
    max_width, max_height = 1920, 1080

    with Image.open(value) as img:
        width, height = img.size

    if width < min_width or height < min_height:
        raise ValidationError(
            _("Минимальный размер фото должен быть 320x240 пикселей.")
        )

    if width > max_width or height > max_height:
        raise ValidationError(
            _("Максимальный размер фото должен быть 1920x1080 пикселей.")
        )


def validate_image(value):
    validate_image_format(value)
    validate_image_size(value)
    validate_image_resolution(value)
