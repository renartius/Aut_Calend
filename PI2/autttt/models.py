from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()

    def __str__(self):
        return self.titulo
