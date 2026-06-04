# 📋 Aplicación To-Do List - Documentación Completa

## 🎯 Resumen General

Aplicación web de lista de tareas (To-Do List) completamente funcional construida con **Flask**, **Jinja2** y **Bootstrap 5**. La aplicación implementa un CRUD básico en memoria con una interfaz gráfica moderna y responsiva.

---

## 📁 Estructura del Proyecto

```
todo_app/
├── run.py                              # 🚀 Punto de entrada principal
├── requirements.txt                    # 📦 Dependencias del proyecto
├── README.md                           # 📚 Este archivo
├── .gitignore                          # 🔒 Archivos a ignorar en Git
│
└── app/                                # 📦 Paquete principal de la aplicación
    ├── __init__.py                     # ⚙️ Factory Pattern - Configuración Flask
    │
    ├── routes/                         # 🛣️ Blueprints (Rutas)
    │   ├── __init__.py
    │   └── tareas.py                   # 🎯 Blueprint CRUD de tareas
    │
    ├── templates/                      # 🎨 Plantillas HTML (Jinja2)
    │   ├── base.html                   # 📄 Plantilla base (navbar, footer, estilos)
    │   └── tareas/
    │       └── index.html              # 📄 Página principal (formulario + lista)
    │
    └── static/                         # 🖼️ Archivos estáticos (CSS, JS, imágenes)
        └── (listos para agregar recursos)
```

---

## 🔧 Configuración e Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Crear un Entorno Virtual

```bash
# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar la Aplicación

```bash
python run.py
```

La aplicación estará disponible en: **http://localhost:5000**

---

## 🏗️ Arquitectura y Patrones Utilizados

### 1. **Application Factory Pattern** (`app/__init__.py`)

La aplicación utiliza el patrón Factory para crear instancias de Flask:

```python
def create_app():
    """Factory function para crear y configurar la aplicación Flask."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    
    # Registrar blueprints
    app.register_blueprint(tareas_bp, url_prefix='/tareas')
    
    return app
```

**Ventajas:**
- ✅ Facilita testing
- ✅ Permite múltiples instancias de la app
- ✅ Separación clara de responsabilidades

### 2. **Blueprints** (`app/routes/tareas.py`)

La lógica de negocio se organiza en Blueprints:

```python
tareas_bp = Blueprint(
    name='tareas',
    import_name=__name__,
    template_folder='../../templates',
    static_folder='../../static'
)
```

**Ventajas:**
- ✅ Modularidad
- ✅ Escalabilidad
- ✅ Reutilización de código
- ✅ Fácil de mantener y extender

### 3. **Almacenamiento en Memoria**

Las tareas se almacenan en una lista global:

```python
tareas_db = []  # Lista global de tareas
contador_id = 0  # Contador autoincremental para IDs

# Estructura de cada tarea
{
    'id': 1,
    'titulo': 'Mi tarea',
    'completada': False
}
```

**Nota:** Este almacenamiento se pierde al reiniciar la aplicación. Para persistencia, usa una base de datos real (SQLite, PostgreSQL, etc.)

---

## 🛣️ Rutas API y Endpoints

### 1. **GET /tareas/** - Listar todas las tareas

**Descripción:** Obtiene todas las tareas y renderiza la interfaz HTML.

**Respuesta:** Plantilla HTML con lista de tareas

**Ejemplo:**
```bash
GET http://localhost:5000/tareas/
```

---

### 2. **POST /tareas/add** - Crear nueva tarea

**Descripción:** Crea una nueva tarea con estado inicial `completada=False`.

**Datos esperados (formulario):**
```html
<form method="POST" action="/tareas/add">
    <input type="text" name="titulo" placeholder="Nueva tarea..." required>
    <button type="submit">Agregar</button>
</form>
```

**Validaciones:**
- ✅ El título es obligatorio
- ✅ El título no puede estar vacío
- ✅ Máximo 200 caracteres

**Comportamiento:**
- Crea la tarea con ID autoincremental
- Redirige a `/tareas/` después de crear

**Ejemplo:**
```bash
POST http://localhost:5000/tareas/add
Data: titulo="Comprar leche"
```

---

### 3. **POST /tareas/toggle/<id>** - Marcar completada/incompleta

**Descripción:** Invierte el estado de completación de una tarea.

**Parámetros:**
- `id` (int): ID de la tarea

**Comportamiento:**
- Si `completada=False` → cambia a `True`
- Si `completada=True` → cambia a `False`
- Redirige a `/tareas/` después de actualizar

**Ejemplo:**
```bash
POST http://localhost:5000/tareas/toggle/1
```

---

### 4. **POST /tareas/delete/<id>** - Eliminar tarea

**Descripción:** Elimina una tarea por su ID.

**Parámetros:**
- `id` (int): ID de la tarea a eliminar

**Comportamiento:**
- Elimina la tarea de la lista
- Redirige a `/tareas/` después de eliminar
- Muestra confirmación antes de eliminar

**Ejemplo:**
```bash
POST http://localhost:5000/tareas/delete/1
```

---

## 🎨 Interfaz Gráfica (UI)

### **base.html** - Plantilla Base

**Características:**
- ✅ Estructura HTML5 semántica
- ✅ Bootstrap 5 desde CDN
- ✅ Font Awesome para iconos
- ✅ Estilos personalizados con gradientes
- ✅ Responsive (mobile-first)
- ✅ Navbar personalizado con branding
- ✅ Footer con información

**Estructura:**
```html
<html>
  <head>
    <!-- CDN Bootstrap 5 -->
    <!-- CDN Font Awesome -->
    <!-- Estilos personalizados -->
  </head>
  <body>
    <!-- Navbar -->
    <!-- Contenedor principal (extends aquí) -->
    <!-- Footer -->
  </body>
</html>
```

**Colores principales:**
- 🟣 Primario: `#4f46e5` (Indigo)
- 🟢 Éxito: `#10b981` (Emerald)
- 🔴 Peligro: `#ef4444` (Red)

---

### **index.html** - Página Principal

**Secciones:**

#### 1️⃣ Formulario de Nueva Tarea
- Campo de entrada para el título
- Botón para agregar
- Validación en tiempo real
- Auto-focus en el campo de entrada

#### 2️⃣ Estadísticas
- Total de tareas
- Tareas completadas
- Actualiza en tiempo real

#### 3️⃣ Lista de Tareas
- ✅ Checkbox para marcar completada
- 📝 Título de la tarea
- 🔄 Botón para cambiar estado
- 🗑️ Botón para eliminar
- 🎨 Estilos diferenciados para tareas completadas (tachadas)

#### 4️⃣ Estado Vacío
- Mensaje cuando no hay tareas
- Icono visual atractivo

---

## 💡 Funcionalidades Implementadas

### ✅ CRUD Completo

| Operación | Método | Ruta | Función |
|-----------|--------|------|----------|
| **Create** | POST | `/tareas/add` | Crear nueva tarea |
| **Read** | GET | `/tareas/` | Listar todas las tareas |
| **Update** | POST | `/tareas/toggle/<id>` | Cambiar estado |
| **Delete** | POST | `/tareas/delete/<id>` | Eliminar tarea |

### ✨ Características de UX

- 🎯 Interfaz intuitiva y limpia
- 📱 Responsiva (funciona en móvil, tablet, desktop)
- ⌨️ Soporte para teclado (Enter en formulario, Tab navegación)
- 🔄 Transiciones suaves y animaciones
- 💾 Confirmación antes de eliminar
- 📊 Estadísticas en tiempo real
- 🎨 Tema moderno con gradientes
- ♿ Accesibilidad (labels, titles, alt text)

---

## 🔐 Seguridad

### Configuración Actual (Desarrollo)
```python
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
```

### ⚠️ Para Producción

1. **Cambiar SECRET_KEY:**
   ```python
   import secrets
   app.config['SECRET_KEY'] = secrets.token_hex(32)
   ```

2. **Usar variables de entorno:**
   ```python
   import os
   app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
   ```

3. **Habilitar HTTPS**

4. **Validar y sanitizar entrada:**
   ```python
   titulo = request.form.get('titulo', '').strip()
   if len(titulo) > 200:
       titulo = titulo[:200]
   ```

5. **Usar una base de datos real**

---

## 📊 Estadísticas del Código

| Archivo | Líneas | Descripción |
|---------|--------|-------------|
| `run.py` | 12 | Punto de entrada |
| `app/__init__.py` | 35 | Factory pattern |
| `app/routes/tareas.py` | 145 | Lógica CRUD |
| `app/templates/base.html` | 150 | Plantilla base |
| `app/templates/index.html` | 250+ | Página principal |
| **Total** | **~600** | **Código completo** |

---

## 🚀 Próximos Pasos y Mejoras

### Corto Plazo
1. ✅ ~~Crear estructura base~~ (Completado)
2. ✅ ~~Implementar CRUD en memoria~~ (Completado)
3. ✅ ~~Crear interfaz HTML~~ (Completado)
4. 🔜 Agregar base de datos (SQLite o PostgreSQL)
5. 🔜 Agregar autenticación de usuarios
6. 🔜 Agregar edición de tareas

### Mediano Plazo
7. 🔜 Categorías/etiquetas para tareas
8. 🔜 Prioridades (Alta, Media, Baja)
9. 🔜 Fechas de vencimiento
10. 🔜 Búsqueda y filtros
11. 🔜 API REST (JSON responses)

### Largo Plazo
12. 🔜 Compartir tareas (colaboración)
13. 🔜 Notificaciones por email
14. 🔜 Integración con calendario
15. 🔜 App móvil (Flutter/React Native)
16. 🔜 Sincronización en tiempo real (WebSockets)

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask 2.3.2** - Framework web minimalista
- **Werkzeug 2.3.6** - Utilidades WSGI
- **Jinja2** - Motor de plantillas

### Frontend
- **HTML5** - Estructura semántica
- **Bootstrap 5** - Framework CSS responsivo
- **Font Awesome** - Iconos vectoriales
- **Vanilla JavaScript** - Interactividad
- **CSS3** - Estilos avanzados (gradientes, animaciones)

### Desarrollo
- **Python 3.8+** - Lenguaje base
- **pip** - Gestor de paquetes
- **venv** - Entorno virtual

---

## 📝 Notas Importantes

### Almacenamiento de Datos

⚠️ **Las tareas se almacenan en memoria y se pierden al reiniciar la aplicación.**

Para persistencia, implementa una de estas opciones:

#### SQLite (Recomendado para desarrollo)
```bash
pip install Flask-SQLAlchemy
```

#### PostgreSQL (Recomendado para producción)
```bash
pip install psycopg2-binary
```

---

## 🐛 Solución de Problemas

### Error: `ModuleNotFoundError: No module named 'flask'`
**Solución:** Asegúrate de que el entorno virtual esté activado e instala las dependencias:
```bash
pip install -r requirements.txt
```

### Error: `Port 5000 already in use`
**Solución:** Cambia el puerto en `run.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Las plantillas no se cargan
**Solución:** Verifica que las rutas de carpetas sean correctas en `tareas.py`:
```python
template_folder='../../templates'  # Ruta correcta
```

### Los estilos no se aplican
**Solución:** Verifica que el CDN de Bootstrap esté accesible (necesita conexión a internet).

---

## 📚 Recursos Útiles

- [Documentación oficial de Flask](https://flask.palletsprojects.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Font Awesome Icons](https://fontawesome.com/icons)

---

## 👨‍💼 Información del Proyecto

- **Versión:** 1.0.0
- **Estado:** 🟢 Funcional
- **Tipo:** Aplicación web educativa
- **Licencia:** Proyecto educativo
- **Mantenedor:** Cloud Camp Learning

---

## 📞 Soporte

Para reportar problemas o sugerencias, crea un issue en el repositorio de GitHub.

---

**¡Gracias por usar la Aplicación To-Do List!** 🎉
