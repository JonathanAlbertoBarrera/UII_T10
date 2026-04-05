from django.urls import path, include
from rest_framework import routers
from .views import ProductoTiendaViewSet

router = routers.DefaultRouter()
router.register(r'tienda', ProductoTiendaViewSet, basename='tienda')

urlpatterns = [
    path('', include(router.urls)),
]