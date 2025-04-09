from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from apps.users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ("level", "correct_answers","last_10_quiz_results_avg","last_login", "date_joined", "balance", "user_code",'auth_provider',)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("full_name","coins",)},
        ),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
            },
        ),
        (_("Important dates"), {"fields": ("level", "correct_answers", "last_10_quiz_results_avg", "last_login", "date_joined","balance", "user_code",'auth_provider')}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "full_name",),
            },
        ),
    )

    list_display = ("email", "full_name", "is_staff",)
    search_fields = ("email", "full_name")
    ordering = ("email",)


