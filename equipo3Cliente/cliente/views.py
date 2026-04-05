from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Clientecompra as Compra
from .serializers import CompraSerializer

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def list_productos_tienda(self, request):
        url_tienda = 'http://127.0.0.1:8001/api/tienda/' 
        try:
            r = requests.get(url_tienda)
            r.raise_for_status()
            productos = r.json()
            return Response(productos)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)