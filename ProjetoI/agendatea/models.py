from django.db import models

# Create your models here.

class Compromisso(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, help_text='')
    pessoa = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tipo} com {self.pessoa} em {self.local} no dia {self.data} às {self.hora}"
