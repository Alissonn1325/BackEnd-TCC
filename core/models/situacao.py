from django.db import models


class Situacao(models.Model):
    status = models.CharField(max_length=30)
    descricao = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"ID: ({self.id}) |:| Status: {self.status} |:| Descrição: {self.descricao}  "
