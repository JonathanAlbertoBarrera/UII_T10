# cliente/serializers.py
from rest_framework import serializers
from .models import Clientecompra as Compra
import requests

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id', 'nombre_cliente', 'fecha', 'total', 'productos']

    def create(self, validated_data):
        productos = validated_data.get('productos', [])
        total = sum(p['cantidad'] * p['precio_unitario'] for p in productos)
        validated_data['total'] = total

        compra = Compra.objects.create(**validated_data)

        for prod in productos:
            prod_id = prod.get('id')
            nombre = prod.get('nombre_producto', 'Producto desconocido')
            if not prod_id:
                print(f"No se puede actualizar stock")
                continue
            try:
                url = f"http://127.0.0.1:8001/api/tienda/{prod_id}/"
                r_get = requests.get(url)
                r_get.raise_for_status()
                stock_actual = r_get.json().get('stock', 0)
                nuevo_stock = max(stock_actual - prod['cantidad'], 0)
                r_patch = requests.patch(url, json={'stock': nuevo_stock})
                r_patch.raise_for_status()
            except Exception as e:
                print(f"Error actualizando stock del producto {nombre}: {e}")

        return compra

    def update(self, instance, validated_data):
        productos_nuevos = validated_data.get('productos', instance.productos)
        productos_anteriores = instance.productos


        total = sum(p['cantidad'] * p['precio_unitario'] for p in productos_nuevos)

        for prod_nuevo in productos_nuevos:
            prod_id = prod_nuevo.get('id')
            if not prod_id:
                continue

            try:
                prod_anterior = next(
                    (p for p in productos_anteriores if p.get('id') == prod_id),
                    None
                )

                cantidad_anterior = prod_anterior.get('cantidad', 0) if prod_anterior else 0
                cantidad_nueva = prod_nuevo.get('cantidad', 0)

                diferencia = cantidad_nueva - cantidad_anterior

                if diferencia == 0:
                    continue

                url = f"http://127.0.0.1:8001/api/tienda/{prod_id}/"

                r_get = requests.get(url)
                r_get.raise_for_status()
                stock_actual = r_get.json().get('stock', 0)

                nuevo_stock = stock_actual - diferencia
                if nuevo_stock < 0:
                    nuevo_stock = 0

                requests.patch(url, json={'stock': nuevo_stock})

            except Exception as e:
                print(f"Error en update: {e}")

        instance.nombre_cliente = validated_data.get('nombre_cliente', instance.nombre_cliente)
        instance.productos = productos_nuevos
        instance.total = total

        instance.save()

        return instance