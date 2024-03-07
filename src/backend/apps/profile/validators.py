from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from PIL import Image


class MinLengthValidator:
    def __init__(self, min_length):
        self.min_length = min_length

    def validate(self, value):
        if len(value) < self.min_length:
            raise ValidationError(
                f"Эта строка должна содержать минимум {self.min_length} символов."
            )


class AgeValidator:
    def __init__(self, min_age=0):
        self.min_age = min_age

    def __call__(self, value):
        today = date.today()

        if value > today:
            raise ValidationError("Дата не может быть в будущем.")


def validate_image_format(value):
    valid_extensions = [".png", ".jpg", ".jpeg"]
    ext = value.name.lower().split(".")[-1]
    if not ext in valid_extensions:
        raise ValidationError(
            "Пожалуйста загрузите файл с расширением PNG или JPEG."
        )


def validate_image_size(value):
    max_size = 10 * 1024 * 1024  # 10 MB
    if value.size > max_size:
        raise ValidationError("Файл не должен превышать размер 10 MB.")


def validate_image_resolution(value):
    min_width, min_height = 320, 240
    max_width, max_height = 1920, 1080

    with Image.open(value) as img:
        width, height = img.size

    if width < min_width or height < min_height:
        raise ValidationError(
            "Минимальный размер фото должен быть 320x240 пикселей."
        )

    if width > max_width or height > max_height:
        raise ValidationError(
            "Максимальный размер фото должен быть 1920x1080 пикселей."
        )


def validate_image(value):
    validate_image_format(value)
    validate_image_size(value)
    validate_image_resolution(value)
