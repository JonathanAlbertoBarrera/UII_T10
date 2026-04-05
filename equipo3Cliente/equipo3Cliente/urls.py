from django.urls import path, include
from rest_framework import routers
from cliente.views import CompraViewSet

router = routers.DefaultRouter()
router.register(r'compras', CompraViewSet, basename='compras')

urlpatterns = [
    path('', include(router.urls)),
    path('productos-tienda/', CompraViewSet.as_view({'get': 'list_productos_tienda'})),
]