# Generated by Django 5.1 on 2024-08-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_situacao_delete_adotante_delete_voluntario_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Especie",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("especie", models.CharField(max_length=100)),
            ],
        ),
    ]
