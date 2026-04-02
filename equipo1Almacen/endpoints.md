# Endpoints API Productos

Base URL: http://localhost:8000/api/productos/

---

## Listar todos (GET)
```cmd
curl http://localhost:8000/api/productos/
```

---

## Ver uno (GET)
```cmd
curl http://localhost:8000/api/productos/1/
```

---

## Crear producto (POST)
```cmd
curl -X POST http://localhost:8000/api/productos/ ^
  -H "Content-Type: application/json" ^
  -d "{\"nombre\":\"Laptop\",\"descripcion\":\"Laptop gaming\",\"precio\":\"15999.99\",\"stock\":10}"
```

---

## Actualizar completo (PUT)
```cmd
curl -X PUT http://localhost:8000/api/productos/1/ ^
  -H "Content-Type: application/json" ^
  -d "{\"nombre\":\"Laptop Pro\",\"descripcion\":\"Actualizada\",\"precio\":\"18999.99\",\"stock\":5}"
```

---

## Actualizar parcial (PATCH)
```cmd
curl -X PATCH http://localhost:8000/api/productos/1/ ^
  -H "Content-Type: application/json" ^
  -d "{\"precio\":\"16500.00\"}"
```

---

## Descontar stock (POST)
```cmd
curl -X POST http://localhost:8000/api/productos/1/descontar_stock/ ^
  -H "Content-Type: application/json" ^
  -d "{\"cantidad\":3}"
```

---

## Eliminar (DELETE)
```cmd
curl -X DELETE http://localhost:8000/api/productos/1/
```
