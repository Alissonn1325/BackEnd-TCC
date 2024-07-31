from django.db import models


class Adotante(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nome} | {self.cpf} | {self.telefone} | {self.email} | {self.endereco}"
