# Generated by Django 5.1.3 on 2024-12-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="situacao",
            options={"verbose_name": "Situação", "verbose_name_plural": "Situações"},
        ),
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="cpf",
        ),
        migrations.RemoveField(
            model_name="user",
            name="foto",
        ),
        migrations.RemoveField(
            model_name="user",
            name="passage_id",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(help_text="Email", max_length=255, unique=True, verbose_name="email"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True, help_text="Indica que este usuário está ativo.", verbose_name="Usuário está ativo"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Indica que este usuário pode acessar o Admin.",
                verbose_name="Usuário é da equipe",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, help_text="Username", max_length=255, null=True, verbose_name="name"),
        ),
    ]
