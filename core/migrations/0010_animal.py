# Generated by Django 5.1 on 2024-08-20 19:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_rename_raca_raca_raca_adocao"),
    ]

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=40)),
                ("idade", models.IntegerField()),
                ("sexo", models.CharField(max_length=10)),
                ("status", models.CharField(max_length=100)),
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="animais", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
