from django.db import models

# Create your models here.

class Pokemon(models.Model):
    IDpoke = models.IntegerField()
    Descripcion = models.CharField(max_length=300)
    Peso = models.DecimalField(decimal_places=2, max_digits=2)
    Altura = models.DecimalField(decimal_places=2, max_digits=2)
        


