from django.db import models

from uploader.models import Image

from .raca import Raca
from .situacao import Situacao


class Animal(models.Model):
    class Sexo(models.IntegerChoices):
        MACHO = 1, "Macho"
        FEMEA = 2, "Fêmea"

    class StatusAnimal(models.IntegerChoices):
        DISPONIVEL = 1, "Disponível"
        ADOTADO = 2, "Adotado"
        EM_TRATAMENTO = 3, "Em tratamento"

    class Especie(models.IntegerChoices):
        CACHORRO = 1, "Cachorro"
        GATO = 2, "Gato"

    nome = models.CharField(max_length=40)
    idade = models.PositiveIntegerField()  
    sexo = models.IntegerField(choices=Sexo.choices)
    especie = models.IntegerField(choices=Especie.choices)
    situacao = models.ForeignKey(Situacao, on_delete=models.SET_NULL, null=True, blank=True)
    raca = models.ForeignKey(Raca, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"
        ordering = ["nome"]
    def __str__(self):
        return f"{self.nome} ({self.especie}) - {self.sexo}"
