from django.db import models


class Raca(models.Model):

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"

    def __str__(self):
        return f"ID: {self.id} |:| Raça: {self.raca}"
