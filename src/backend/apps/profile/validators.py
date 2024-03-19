from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from PIL import Image


class BirthdayValidator:
    """Валидатор, не позволяющий пользователю добавить будущую дату в качестве своего дня рождения"""

    def __init__(self, min_age=0):
        self.min_age = min_age

    def __call__(self, value):
        today = date.today()

        if value > today:
            raise ValidationError("Дата не может быть в будущем.")


def validate_image_format(value):
    """Валидатор, позволяющий добавить аватар только определенного формата .png, .jpg или .jpeg"""
    valid_extensions = [".png", ".jpg", ".jpeg"]
    ext = value.name.lower().split(".")[-1]
    if not ext in valid_extensions:
        raise ValidationError(
            "Пожалуйста загрузите файл с расширением PNG или JPEG."
        )


def validate_image_size(value):
    """Валидатор, не позволяющий загрузить картинку размером больше 10 MB"""
    max_size = 10 * 1024 * 1024  # 10 MB
    if value.size > max_size:
        raise ValidationError("Файл не должен превышать размер 10 MB.")


def validate_image_resolution(value):
    """Валидатор, ограничивающий размер картинки"""
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

    # Проверяем соотвествие видимости общего профиля - видимости контактов


def visibility_correspondence(value, profile):
    if profile.visibile_status == 2 or profile.visibile_status == 3:
        if value != 2 and value != 3:
            raise ValidationError(
                "Видимость контактов не должна противоречить видимости профиля"
            )
    elif profile.visibile_status == 3:
        if value != 3:
            raise ValidationError(
                "Видимость контактов не должна противоречить видимости профиля"
            )
