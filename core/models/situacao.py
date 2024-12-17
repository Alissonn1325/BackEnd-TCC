from django.db import models


class Situacao(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.status}"

    class Meta:
        verbose_name = "Situação"
        verbose_name_plural = "Situações"