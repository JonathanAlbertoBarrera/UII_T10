from django.db import models

class ProductoTienda(models.Model):
    id_almacen = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre