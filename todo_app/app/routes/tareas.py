"""Blueprint para gestionar operaciones CRUD de tareas (To-Do List).

Arquitectura:
- Implementa un CRUD básico en memoria utilizando una estructura de datos global
- Las tareas se almacenan en una lista de diccionarios
- Cada tarea tiene: id (único), titulo, completada (boolean)
- Validar datos de entrada y retornar respuestas JSON o redirigir según se requiera

Flujo:
- GET: Retorna datos (JSON o plantilla HTML)
- POST: Modifica datos y redirige a la vista principal
"""

from flask import Blueprint, request, render_template, redirect, url_for

# Crear Blueprint para las rutas de tareas
# Prefijo '/tareas' se añade en __init__.py
tareas_bp = Blueprint(
    name='tareas',
    import_name=__name__,
    url_prefix='',  # El prefijo se aplica en el registro en __init__.py
    template_folder='../../templates',  # Ruta a la carpeta de templates
    static_folder='../../static'  # Ruta a la carpeta de static
)

# ============================================================================
# ALMACENAMIENTO EN MEMORIA
# ============================================================================
# Estructura de datos global para almacenar tareas
# Formato: {
#     'id': int,
#     'titulo': str,
#     'completada': bool
# }
tareas_db = []
contador_id = 0  # Contador para generar IDs únicos


def obtener_siguiente_id():
    """Genera el siguiente ID disponible para una nueva tarea."""
    global contador_id
    contador_id += 1
    return contador_id


# ============================================================================
# RUTAS CRUD
# ============================================================================

@tareas_bp.route('/', methods=['GET'])
def obtener_todas_las_tareas():
    """Obtener todas las tareas y renderizar la plantilla index.html.
    
    Método HTTP: GET
    Ruta: /tareas/
    
    Funcionalidad:
    - Retorna la plantilla HTML con la lista completa de tareas
    - Incluye tareas completadas e incompletas
    - Renderiza el formulario para añadir nuevas tareas
    
    Context esperado en la plantilla:
    {
        'tareas': [
            {'id': 1, 'titulo': 'Tarea 1', 'completada': False},
            {'id': 2, 'titulo': 'Tarea 2', 'completada': True}
        ]
    }
    """
    return render_template('index.html', tareas=tareas_db)


@tareas_bp.route('/add', methods=['POST'])
def crear_nueva_tarea():
    """Crear una nueva tarea y redirigir a la vista principal.
    
    Método HTTP: POST
    Ruta: /tareas/add
    
    Datos esperados (formulario o JSON):
    {
        'titulo': str (requerido, no vacío)
    }
    
    Validaciones:
    - El título es obligatorio y no puede estar vacío
    - El título se elimina de espacios en blanco
    
    Comportamiento:
    - Crea una nueva tarea con ID autoincremental
    - Estado inicial: completada = False
    - Redirige a /tareas/ después de crear
    
    Errores posibles:
    - Título vacío o no proporcionado -> redirige sin crear
    """
    titulo = request.form.get('titulo', '').strip()
    
    # Validar que el título no esté vacío
    if titulo:
        nueva_tarea = {
            'id': obtener_siguiente_id(),
            'titulo': titulo,
            'completada': False
        }
        tareas_db.append(nueva_tarea)
    
    # Redirigir a la vista principal
    return redirect(url_for('tareas.obtener_todas_las_tareas'))


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
    - Redirige a /tareas/ después de actualizar
    
    Comportamiento en caso de error:
    - Si el ID no existe, redirige sin hacer cambios
    """
    # Buscar la tarea por ID
    for tarea in tareas_db:
        if tarea['id'] == id:
            # Invertir el estado de completación
            tarea['completada'] = not tarea['completada']
            break
    
    # Redirigir a la vista principal
    return redirect(url_for('tareas.obtener_todas_las_tareas'))


@tareas_bp.route('/delete/<int:id>', methods=['POST'])
def eliminar_tarea(id):
    """Eliminar una tarea por su ID.
    
    Método HTTP: POST
    Ruta: /tareas/delete/<id>
    Parámetro: id (int) - ID de la tarea a eliminar
    
    Funcionalidad:
    - Busca la tarea con el ID especificado
    - La elimina del almacenamiento en memoria
    - Redirige a /tareas/ después de eliminar
    
    Comportamiento en caso de error:
    - Si el ID no existe, redirige sin hacer cambios
    """
    global tareas_db
    
    # Filtrar la tarea con el ID especificado
    tareas_db = [tarea for tarea in tareas_db if tarea['id'] != id]
    
    # Redirigir a la vista principal
    return redirect(url_for('tareas.obtener_todas_las_tareas'))
