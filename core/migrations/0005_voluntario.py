# Generated by Django 5.0.6 on 2024-07-31 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_adotante_cpf_alter_adotante_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Voluntario",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("cpf", models.CharField(max_length=11)),
                ("telefone", models.CharField(max_length=13)),
                ("email", models.EmailField(max_length=100)),
            ],
        ),
    ]
