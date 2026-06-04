"""Blueprint para gestionar operaciones CRUD de tareas (To-Do List).

Arquitectura:
- Implementa un CRUD básico en memoria utilizando una estructura de datos global
- Las tareas se almacenan en una lista de diccionarios
- Cada tarea tiene: id (único), titulo, descripcion, completada (boolean)
- Validar datos de entrada y retornar respuestas JSON con códigos HTTP apropiados

Estandarización de respuestas:
- Éxito (200, 201): {'success': True, 'data': {...}, 'mensaje': '...'}
- Error (400, 404): {'success': False, 'error': '...', 'codigo': '...'}
"""

from flask import Blueprint, request, jsonify

# Crear Blueprint para las rutas de tareas
# Prefijo '/tareas' se añade en __init__.py
tareas_bp = Blueprint(
    name='tareas',
    import_name=__name__,
    url_prefix='',  # El prefijo se aplica en el registro en __init__.py
    template_folder='../templates/tareas',
    static_folder='../static'
)

# ============================================================================
# ALMACENAMIENTO EN MEMORIA
# ============================================================================
# Estructura de datos global para almacenar tareas
# Formato: {
#     'id': int,
#     'titulo': str,
#     'descripcion': str,
#     'completada': bool
# }
tareas_db = []
counter_id = 0  # Contador para generar IDs únicos


# ============================================================================
# RUTAS CRUD
# ============================================================================

@tareas_bp.route('/', methods=['GET'])
def obtener_todas_las_tareas():
    """Obtener todas las tareas.
    
    Método HTTP: GET
    Ruta: /tareas/
    
    Funcionalidad:
    - Retorna la lista completa de tareas almacenadas en memoria
    - Incluye tareas completadas e incompletas
    
    Respuesta esperada (200 OK):
    {
        'success': True,
        'data': [
            {'id': 1, 'titulo': 'Tarea 1', 'descripcion': '...', 'completada': False},
            {'id': 2, 'titulo': 'Tarea 2', 'descripcion': '...', 'completada': True}
        ],
        'total': 2
    }
    """
    pass


@tareas_bp.route('/add', methods=['POST'])
def crear_nueva_tarea():
    """Crear una nueva tarea.
    
    Método HTTP: POST
    Ruta: /tareas/add
    
    Datos esperados (JSON):
    {
        'titulo': str (requerido, no vacío),
        'descripcion': str (opcional, default: '')
    }
    
    Validaciones:
    - El título es obligatorio y no puede estar vacío
    - La descripción es opcional
    
    Respuesta esperada (201 Created):
    {
        'success': True,
        'data': {
            'id': 3,
            'titulo': 'Nueva tarea',
            'descripcion': '...',
            'completada': False
        },
        'mensaje': 'Tarea creada exitosamente'
    }
    
    Errores posibles (400 Bad Request):
    - Título vacío o no proporcionado
    - Formato JSON inválido
    """
    pass


@tareas_bp.route('/toggle/<int:id>', methods=['POST'])
def toggle_tarea(id):
    """Marcar una tarea como completada o incompleta (toggle).
    
    Método HTTP: POST
    Ruta: /tareas/toggle/<id>
    Parámetro: id (int) - ID de la tarea a actualizar
    
    Funcionalidad:
    - Invierte el estado de completación de la tarea
    - Si completada=False, pasa a True
    - Si completada=True, pasa a False
    
    Respuesta esperada (200 OK):
    {
        'success': True,
        'data': {
            'id': 1,
            'titulo': 'Tarea 1',
            'descripcion': '...',
            'completada': True  # Ahora es True (antes era False)
        },
        'mensaje': 'Tarea actualizada exitosamente'
    }
    
    Errores posibles (404 Not Found):
    - ID de tarea no existe
    """
    pass


@tareas_bp.route('/delete/<int:id>', methods=['POST'])
def eliminar_tarea(id):
    """Eliminar una tarea por su ID.
    
    Método HTTP: POST
    Ruta: /tareas/delete/<id>
    Parámetro: id (int) - ID de la tarea a eliminar
    
    Funcionalidad:
    - Busca la tarea con el ID especificado
    - La elimina del almacenamiento en memoria
    - Retorna confirmación de eliminación
    
    Respuesta esperada (200 OK):
    {
        'success': True,
        'data': {
            'id': 1,
            'titulo': 'Tarea eliminada',
            'descripcion': '...',
            'completada': False
        },
        'mensaje': 'Tarea eliminada exitosamente'
    }
    
    Errores posibles (404 Not Found):
    - ID de tarea no existe
    """
    pass
