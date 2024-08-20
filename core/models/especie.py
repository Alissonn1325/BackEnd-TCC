from django.db import models


class Especie(models.Model):
    especie = models.CharField(max_length=100)

    def __str__(self):
        return f"ID: ({self.id}) |:| Espécie: {self.especie} |:|"
