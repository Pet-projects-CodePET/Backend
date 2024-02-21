from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.forms import UserAdminChangeForm, UserAdminCreationForm


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    """Класс для настройки регистрации модели пользователей в админ зоне."""

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            _("Personal info"),
            {"fields": ("email",)},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login",)},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = (
        "email",
        "username",
        "is_active",
        "is_staff",
    )
    list_editable = ("is_staff",)
    list_filter = (
        "email",
        "username",
    )
    ordering = (
        "created",
        "username",
    )
