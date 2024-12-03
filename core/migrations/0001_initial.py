# Generated by Django 5.1.3 on 2024-12-03 16:57

import core.models.user
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Raca",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("raca", models.TextField(blank=True, max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Raça",
                "verbose_name_plural": "Raças",
            },
        ),
        migrations.CreateModel(
            name="Situacao",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(max_length=30)),
                ("descricao", models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("passage_id", models.CharField(max_length=255, unique=True)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.TextField()),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="uploader.image",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuário",
                "verbose_name_plural": "Usuários",
            },
            managers=[
                ("objects", core.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Adocao",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("data_adocao", models.DateField()),
                ("observacoes", models.TextField(blank=True, max_length=500, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="adocoes", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "Adoção",
                "verbose_name_plural": "Adoções",
            },
        ),
        migrations.CreateModel(
            name="Animal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=40)),
                ("idade", models.PositiveIntegerField()),
                ("sexo", models.IntegerField(choices=[(1, "Macho"), (2, "Fêmea")])),
                ("status", models.IntegerField(choices=[(1, "Disponível"), (2, "Adotado"), (3, "Em tratamento")])),
                ("especie", models.IntegerField(choices=[(1, "Cachorro"), (2, "Gato")])),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="uploader.image",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="animais", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "raca",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="core.raca"
                    ),
                ),
                (
                    "situacao",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="core.situacao"
                    ),
                ),
            ],
            options={
                "verbose_name": "Animal",
                "verbose_name_plural": "Animais",
                "ordering": ["nome"],
            },
        ),
    ]
