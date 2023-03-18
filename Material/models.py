from django.db import models

# Create your models here.

class Material(models.Model):

    id_material = models.AutoField(primary_key=True)
    nombre_material = models.CharField(
        'Nombre de Material', max_length=50, blank=False, unique=True)
        

    class Meta:
        verbose_name = ("Material")
        verbose_name_plural = ("Materiales")

    def __str__(self):
        return self.nombre_material


