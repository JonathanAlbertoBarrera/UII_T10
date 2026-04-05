from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
	queryset = Producto.objects.all().order_by('-id')
	serializer_class = ProductoSerializer

	@action(detail=True, methods=['post'])
	def descontar_stock(self, request, pk=None):
		producto = self.get_object()
		cantidad = request.data.get('cantidad')

		try:
			cantidad = int(cantidad)
		except (TypeError, ValueError):
			return Response(
				{'detail': 'La cantidad debe ser un numero entero.'},
				status=status.HTTP_400_BAD_REQUEST,
			)

		if cantidad <= 0:
			return Response(
				{'detail': 'La cantidad debe ser mayor a 0.'},
				status=status.HTTP_400_BAD_REQUEST,
			)

		if cantidad > producto.stock:
			return Response(
				{'detail': 'Stock insuficiente para completar la operacion.'},
				status=status.HTTP_400_BAD_REQUEST,
			)

		producto.stock -= cantidad
		producto.save(update_fields=['stock'])

		return Response(
			{
				'detail': 'Stock actualizado correctamente.',
				'id': producto.id,
				'stock_actual': producto.stock,
			},
			status=status.HTTP_200_OK,
		)
