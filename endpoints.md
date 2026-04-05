# Endpoints API — Equipo 2: Tienda

Base URL: http://localhost:8001/api/tienda/

Listar todos los productos (GET)
curl http://localhost:8001/api/tienda/

Ver un producto (GET)
curl http://localhost:8001/api/tienda/1/

Crear producto en la tienda (POST)
curl -X POST http://localhost:8001/api/tienda/ ^
  -H "Content-Type: application/json" ^
  -d "{\"id_almacen\":1,\"nombre\":\"Coca-Cola\",\"descripcion\":\"La mejor\",\"precio\":22.0,\"stock\":20}"

Actualizar completo (PUT)
curl -X PUT http://localhost:8001/api/tienda/1/ ^
  -H "Content-Type: application/json" ^
  -d "{\"id_almacen\":1,\"nombre\":\"Coca-Cola Zero\",\"descripcion\":\"Sin azúcar\",\"precio\":24.0,\"stock\":15}"

Actualizar parcial (PATCH)
curl -X PATCH http://localhost:8001/api/tienda/1/ ^
  -H "Content-Type: application/json" ^
  -d "{\"precio\":23.0}"

Sincronizar productos desde el Almacén (POST)
curl -X POST http://localhost:8001/api/tienda/sync/
⚠️ Trae los productos del Equipo 1 (Almacén) y los actualiza o crea en la tienda.

Eliminar producto (DELETE)
curl -X DELETE http://localhost:8001/api/tienda/1/