from django.db import models


class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nome} | {self.cpf} | {self.telefone} | {self.email}"
