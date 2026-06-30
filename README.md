# Trabajo Práctico – Sistema de Gestión de Inventario y Depósitos

## Grupo 2

**Integrantes:**

* Thomas Solda
* Lucas Olivares
* Emanuel Uria

## Descripción del Proyecto

El presente trabajo práctico tiene como objetivo diseñar y desarrollar un sistema de gestión de inventario y depósitos orientado a optimizar el control y la administración de productos almacenados. La aplicación permite registrar y consultar información relacionada con el stock disponible, así como gestionar la operación de distintos módulos del negocio: órdenes de producción, materias primas, maquinaria, operadores y líneas de producción.

El sistema busca ofrecer una solución clara y organizada para el seguimiento de inventarios, la actualización de existencias y la administración centralizada de recursos dentro de una organización.

## Tecnologías

El desarrollo del proyecto se realiza con **Django** como framework principal, utilizando su arquitectura basada en apps para separar responsabilidades y facilitar el mantenimiento del código. Además, se emplean herramientas estándar para la persistencia de datos, la definición de modelos y la exposición de rutas de acceso.

## Objetivo General

Desarrollar una aplicación web que permita administrar inventarios y depósitos de manera centralizada, garantizando la integridad de la información y facilitando la gestión de stock, producción y operaciones del sistema.

## Estructura del proyecto

La aplicación está organizada en módulos independientes, cada uno con su propia lógica de negocio y acceso a datos:

- `tp_integrador/`: configuración principal del proyecto, URLs globales y ajustes generales de Django.
- `machinery/`: gestión de la maquinaria del sistema.
- `operators/`: administración de operadores.
- `production_lines/`: manejo de líneas de producción.
- `production_orders/`: gestión de órdenes de producción.
- `products/`: gestión de productos.
- `raw_materials/`: administración de materias primas.

Cada módulo cuenta con carpetas como `controllers/`, `services/`, `repositories/`, `models/`, `validators/`, `dto/` y `exceptions/` para separar responsabilidades.

## Endpoints disponibles

El proyecto expone las siguientes rutas principales para interactuar con la API del sistema:

### Órdenes de producción
- `GET /production-orders/` - listar órdenes de producción.
- `POST /production-orders/create/` - crear una nueva orden.
- `GET /production-orders/<int:order_id>/` - obtener una orden por ID.
- `PATCH /production-orders/<int:order_id>/status/` - modificar el estado de una orden.

### Materias primas
- `GET /raw-materials/` - listar materias primas.
- `POST /raw-materials/create/` - crear una nueva materia prima.
- `GET /raw-materials/<int:material_id>/` - obtener una materia prima por ID.
- `PATCH /raw-materials/<int:material_id>/stock/` - actualizar el stock.

### Maquinaria
- `GET /machinery/` - listar maquinaria.
- `GET /machinery/<int:machine_id>/` - obtener una máquina por ID.
- `PATCH /machinery/<int:machine_id>/status/` - cambiar el estado de una máquina.

### Operadores
- `GET /operators/` - listar operadores.
- `POST /operators/create/` - crear un operador.
- `GET /operators/<int:operator_id>/` - obtener un operador por ID.
- `PATCH /operators/<int:operator_id>/activate/` - activar un operador.
- `PATCH /operators/<int:operator_id>/deactivate/` - desactivar un operador.

### Líneas de producción
- `GET /production-lines/` - listar líneas de producción.
- `GET /production-lines/<int:line_id>/` - obtener una línea por ID.
- `PATCH /production-lines/<int:line_id>/activate/` - activar una línea.
- `PATCH /production-lines/<int:line_id>/deactivate/` - desactivar una línea.

### Inicio del proyecto
- `GET /` - página de inicio básica con enlaces a las rutas principales.

## Cómo inicializar el proyecto

1. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

4. Crear un superusuario (opcional, para acceder al panel de administración):
   ```bash
   python manage.py createsuperuser
   ```

5. Levantar el servidor:
   ```bash
   python manage.py runserver
   ```

Una vez iniciado, la aplicación estará disponible en `http://localhost:8000/`.
