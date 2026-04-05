import requests

# URL del equipo 1 (Almacén)
URL_ALMACEN = 'http://127.0.0.1:8000/api/productos/'

# URL de tu API (Tienda)
URL_TIENDA = 'http://127.0.0.1:8001/api/tienda/'

# Traer productos del equipo 1
r = requests.get(URL_ALMACEN)
if r.status_code != 200:
    print("Error al traer productos del almacén:", r.status_code)
    exit()

productos = r.json()

# Guardar o actualizar productos en tu tienda
for prod in productos:
    response = requests.post(
        URL_TIENDA,
        data={
            'id_almacen': prod['id'],
            'nombre': prod['nombre'],
            'descripcion': prod.get('descripcion', ''),
            'precio': prod['precio'],
            'stock': prod['stock'],
        }
    )
    if response.status_code in [200, 201]:
        print(f"Producto '{prod['nombre']}' guardado/actualizado correctamente")
    else:
        print(f"Error con el producto '{prod['nombre']}':", response.text)