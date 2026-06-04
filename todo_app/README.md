# Aplicación To-Do List con Flask

## Descripción

Aplicación web de lista de tareas (To-Do List) construida con Flask, siguiendo las mejores prácticas de desarrollo en Python.

## Características de Arquitectura

- **Blueprints**: Separación de la lógica de negocio mediante Blueprints de Flask
- **Application Factory**: Patrón de fábrica para crear instancias de la aplicación
- **CRUD en Memoria**: Almacenamiento básico de tareas utilizando estructuras de datos Python
- **API RESTful**: Rutas HTTP estandarizadas para operaciones CRUD
- **Estructura Modular**: Carpetas separadas para templates, static y rutas

## Estructura de Carpetas

```
todo_app/
├── run.py                          # Archivo de entrada principal
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Este archivo
├── .gitignore                      # Archivos a ignorar en Git
└── app/                            # Paquete principal de la aplicación
    ├── __init__.py                 # Factory de la aplicación Flask
    ├── routes/                     # Blueprints de rutas
    │   ├── __init__.py
    │   └── tareas.py               # Blueprint para operaciones CRUD de tareas
    ├── templates/                  # Plantillas HTML
    │   └── tareas/                 # Plantillas específicas del blueprint tareas
    └── static/                     # Archivos estáticos (CSS, JS, imágenes)
```

## Instalación y Configuración

### 1. Crear un entorno virtual

```bash
python -m venv venv
```

### 2. Activar el entorno virtual

**En Linux/Mac:**
```bash
source venv/bin/activate
```

**En Windows:**
```bash
venv\\Scripts\\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python run.py
```

La aplicación estará disponible en `http://localhost:5000`

## API Endpoints

### Obtener todas las tareas
- **Método**: `GET`
- **Ruta**: `/tareas/`
- **Descripción**: Retorna la lista completa de tareas

### Crear una nueva tarea
- **Método**: `POST`
- **Ruta**: `/tareas/add`
- **Body esperado**:
  ```json
  {
    "titulo": "Nombre de la tarea",
    "descripcion": "Descripción opcional"
  }
  ```

### Marcar tarea como completada/incompleta
- **Método**: `POST`
- **Ruta**: `/tareas/toggle/<id>`
- **Descripción**: Invierte el estado de completación de la tarea

### Eliminar una tarea
- **Método**: `POST`
- **Ruta**: `/tareas/delete/<id>`
- **Descripción**: Elimina la tarea con el ID especificado

## Próximos Pasos

1. ✅ Estructura base de la aplicación (completado)
2. ⏳ Implementar lógica CRUD en `app/routes/tareas.py`
3. ⏳ Crear plantillas HTML en `app/templates/tareas/`
4. ⏳ Agregar validaciones y manejo de errores
5. ⏳ Implementar pruebas unitarias

## Tecnologías Utilizadas

- **Flask 2.3.2**: Framework web minimalista para Python
- **Python 3.8+**: Lenguaje de programación
- **Werkzeug 2.3.6**: Utilidades WSGI

## Notas de Desarrollo

- La aplicación utiliza almacenamiento en memoria, por lo que los datos se pierden al reiniciar
- En producción, se recomienda usar una base de datos real (SQLite, PostgreSQL, etc.)
- Para servir la aplicación en producción, utiliza un servidor WSGI como Gunicorn

## Licencia

Proyecto educativo
