from django.db import models

from .user import User


class Adocao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adocoes")
    data_adocao = models.DateField()
    observacoes = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Adoção"
        verbose_name_plural = "Adoções"

    def __str__(self):
        return f"ID: {self.id} |:| Usuário: {self.user} |:| Data: {self.data_adocao}"
