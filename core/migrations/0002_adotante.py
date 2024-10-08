# Generated by Django 5.0.6 on 2024-07-31 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Adotante",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("cpf", models.IntegerField(max_length=11)),
                ("telefone", models.IntegerField(max_length=13)),
                ("email", models.CharField(max_length=100)),
                ("endereco", models.CharField(max_length=60)),
            ],
        ),
    ]
