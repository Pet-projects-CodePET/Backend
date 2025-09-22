from rest_framework import serializers


class NullableDateField(serializers.DateField):
    """Поле даты, которое позволяет передавать пустую строку ("") как None."""

    def to_internal_value(self, value):
        if value in ("", None):
            return None
        return super().to_internal_value(value)
