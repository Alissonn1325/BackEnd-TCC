# Generated by Django 5.1.3 on 2024-12-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_remove_animal_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="contact",
            field=models.CharField(blank=True, help_text="Contact", max_length=255, null=True, verbose_name="contact"),
        ),
    ]
