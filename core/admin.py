"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models
from core.models import Adocao, Animal, Raca, Situacao, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
       (_("Personal Info"), {"fields": ("name","foto")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
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
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    ) 

@admin.register(Adocao)
class AdocaoAdmin(admin.ModelAdmin):
    list_display = ('user', 'data_adocao', 'observacoes')
    search_fields = ('user', 'data_adocao',)
    list_filter = ('data_adocao',)
    ordering = ('user', 'data_adocao', 'observacoes')
    list_per_page = 10

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('foto', 'nome', 'idade', 'sexo', 'status', 'especie', 'situacao', 'raca', 'user')
    search_fields = ('nome', 'raca__nome')
    list_filter = ('sexo', 'status', 'especie', 'situacao', 'raca')
    ordering = ('nome')
    list_per_page = 10

@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('raca',)
    search_fields = ('raca',)
    list_filter = ('raca',)
    ordering = ('raca',)
    list_per_page = 10

@admin.register(Situacao)
class SituacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'categoria')
    search_fields = ('titulo', 'editora__nome', 'categoria__descricao')
    list_filter = ('editora', 'categoria')
    ordering = ('titulo', 'editora', 'categoria')
    list_per_page = 25
