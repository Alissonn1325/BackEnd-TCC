# Generated by Django 5.1.3 on 2024-12-16 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_user_contact"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="contact",
        ),
    ]