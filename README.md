# Trabajo Practico Integrador - ERP de Produccion y Manufactura

**Alumno:** Emanuel Uria

## Descripcion

API REST construida con Django para gestionar procesos de produccion y manufactura. El sistema usa una arquitectura backend por capas y responde siempre en formato JSON mediante `JsonResponse`.

## Arquitectura

Cada app respeta la separacion:

- `controllers`: recibe HTTP, llama al service y devuelve JSON.
- `services`: concentra reglas de negocio y excepciones de dominio.
- `repositories`: administra datos en memoria con listas Python.
- `models`: clases Python puras del dominio.
- `dto`: define los campos expuestos al cliente.
- `validators`: valida datos de entrada.
- `exceptions`: errores de dominio con `message` y `status_code`.

## Modulos

- `production_orders`: ordenes de produccion.
- `raw_materials`: materias primas y alertas de stock minimo.
- `machinery`: maquinaria y estados operativos.
- `operators`: operarios activos e inactivos.
- `production_lines`: lineas de produccion con validacion de maquinaria.

## Endpoints principales

- `GET /production-orders/`
- `POST /production-orders/create/`
- `GET /production-orders/<id>/`
- `PATCH /production-orders/<id>/status/`
- `GET /raw-materials/`
- `POST /raw-materials/create/`
- `PATCH /raw-materials/<id>/stock/`
- `GET /machinery/`
- `PATCH /machinery/<id>/status/`
- `GET /operators/`
- `POST /operators/create/`
- `POST /operators/<id>/activate/`
- `POST /operators/<id>/deactivate/`
- `GET /production-lines/`
- `POST /production-lines/<id>/activate/`
- `POST /production-lines/<id>/deactivate/`

## Ejecucion

```bash
pip install -r requirements.txt
python manage.py test
python manage.py runserver
```
