IMPORTANTE: LA URL DEPENDE DEL PUERTO DONDE HAYAS ARRANCADO EL PROYECTO.
ACCIÓN: CREAR COMPRA
METODO: POST 
URL: http://127.0.0.1:8002/compras/
CUERPO:
{
  "nombre_cliente": "Oscar Montes",
  "productos": [
    { 
        "id":1,
        "nombre_producto": "1",
        "cantidad": 10,
        "precio_unitario":12 
    }
   
  ]
}
ACCIÓN: VISUALIZAR PRODUCTOS EN TIENDA
METODO: GET
URL : http://127.0.0.1:8002/productos-tienda/ 

ACCIÓN: OBTENER COMPRA EN ID ESPECIFICO
METODO: GET
URL: http://127.0.0.1:8002/compras/<id>/

ACCIÓN: ACTULIZACIÓN COMPLETA O PARCIAL
METODO: PUT, PATCH
URL: http://127.0.0.1:8002/compras/<id>/
CUERPO: 

{
    "nombre_cliente":"Oscar MONTES",
  "productos": [
    {
      "id": 1,
      "nombre_producto": "CHOCOLATE",
      "cantidad": 2,
      "precio_unitario": 250
    }
  ]
}

ACCIÓN: ELIMINACION FISICA DE COMPRA
METODO: DELETE
URL: http://127.0.0.1:8002/compras/<id>/

