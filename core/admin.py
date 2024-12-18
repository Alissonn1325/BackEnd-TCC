from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["email"]  
    list_display = ["email", "name", "is_active", "is_staff", "is_superuser"]  
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),  
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "contact",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
    )

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Situacao)
admin.site.register(models.Raca)
admin.site.register(models.Adocao)
admin.site.register(models.Animal)
