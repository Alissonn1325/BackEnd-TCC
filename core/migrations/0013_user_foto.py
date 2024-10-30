# Generated by Django 5.1.1 on 2024-09-10 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_delete_especie_animal_especie_alter_animal_sexo_and_more"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="foto",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]