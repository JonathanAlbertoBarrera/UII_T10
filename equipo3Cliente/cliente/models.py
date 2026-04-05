from django.db import models
from django.utils import timezone

class Clientecompra(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.FloatField(default=0)
    productos = models.JSONField(default=list)  

    def __str__(self):
        return f"Compra de {self.nombre_cliente} - Total: {self.total}"