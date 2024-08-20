from django.db import models


class Raca(models.Model):
    raca = models.CharField(max_length=100)

    def __str__(self):
        return f"ID: ({self.id}) |:| Raça: {self.raca} |:|"
