from rest_framework import serializers
from .models import ProductoTienda

class ProductoTiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoTienda
        fields = '__all__'