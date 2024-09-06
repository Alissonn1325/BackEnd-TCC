from django.db import models
from uploader.models import Image

from .raca import Raca
from .situacao import Situacao
from .user import User


class Animal(models.Model):
    nome = models.CharField(max_length=40)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)
    status = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="animais")
    situacao = models.ForeignKey(Situacao, on_delete=models.SET_NULL, null=True, blank=True)
    raca = models.ForeignKey(Raca, on_delete=models.SET_NULL, null=True, blank=True)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.nome} ({self.sexo}) - {self.status}"

    # SEXO_CHOICES = [
    #     ('Macho', 'Macho'),
    #     ('Fêmea', 'Fêmea'),
    # ]

    # STATUS_CHOICES = [
    #     ('Disponível', 'Disponível'),
    #     ('Adotado', 'Adotado'),
    #     ('Em tratamento', 'Em tratamento'),
    # ]

    # choices=SEXO_CHOICES
    # choices=STATUS_CHOICES
