from django.db import models

from .user import User


class Adocao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adocoes")
    data_adocao = models.DateField()
    observacoes = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"ID: {self.id} |:| Usuario: {self.user}"
