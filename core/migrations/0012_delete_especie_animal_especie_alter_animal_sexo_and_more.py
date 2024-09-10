# Generated by Django 5.1.1 on 2024-09-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_animal_foto"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Especie",
        ),
        migrations.AddField(
            model_name="animal",
            name="especie",
            field=models.IntegerField(choices=[(1, "Cachorro"), (2, "Gato")], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="animal",
            name="sexo",
            field=models.IntegerField(choices=[(1, "Macho"), (2, "Fêmea")]),
        ),
        migrations.AlterField(
            model_name="animal",
            name="status",
            field=models.IntegerField(choices=[(1, "Disponível"), (2, "Adotado"), (3, "Em tratamento")]),
        ),
    ]
