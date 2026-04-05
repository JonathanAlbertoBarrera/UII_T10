from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import requests

from .models import ProductoTienda
from .serializers import ProductoTiendaSerializer

class ProductoTiendaViewSet(viewsets.ModelViewSet):
    queryset = ProductoTienda.objects.all()
    serializer_class = ProductoTiendaSerializer

    @action(detail=False, methods=['post'])
    def sync(self, request):
        url_almacen = 'http://127.0.0.1:8000/api/productos/'  
        try:
            r = requests.get(url_almacen)
            r.raise_for_status()
            productos = r.json()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        for prod in productos:
            ProductoTienda.objects.update_or_create(
                id_almacen=prod['id'],  
                defaults={
                    'nombre': prod['nombre'],
                    'descripcion': prod.get('descripcion', ''),
                    'precio': prod.get('precio', 0),
                    'stock': prod.get('stock', 0),
                }
            )

        return Response({'detail': 'Productos sincronizados correctamente.'}, status=status.HTTP_200_OK)