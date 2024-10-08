# Generated by Django 5.1 on 2024-08-20 19:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_raca"),
    ]

    operations = [
        migrations.RenameField(
            model_name="raca",
            old_name="Raca",
            new_name="raca",
        ),
        migrations.CreateModel(
            name="Adocao",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("data_adocao", models.DateField()),
                ("observacoes", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="adocoes", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
