"""Inicialización y configuración de la aplicación Flask.

Este módulo:
- Crea la instancia de Flask
- Registra los Blueprints
- Configura la aplicación

Arquitectura:
- Utiliza el patrón Application Factory para crear la app de Flask
- Implementa Blueprints para separar la lógica de negocio
"""

from flask import Flask
from app.routes.tareas import tareas_bp


def create_app():
    """Factory function para crear y configurar la aplicación Flask.
    
    Returns:
        Flask: Instancia configurada de la aplicación Flask
    """
    # Crear instancia de Flask
    app = Flask(__name__)
    
    # Configuración de la aplicación
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    app.config['JSON_SORT_KEYS'] = False
    
    # Registrar blueprints
    # El Blueprint 'tareas' maneja todas las operaciones CRUD de tareas
    app.register_blueprint(tareas_bp, url_prefix='/tareas')
    
    # Ruta raíz para verificar que la aplicación está corriendo
    @app.route('/')
    def index():
        """Ruta raíz - página de bienvenida."""
        return {
            'mensaje': 'Bienvenido a la aplicación To-Do List',
            'documentacion': 'Accede a /tareas para gestionar tareas'
        }, 200
    
    return app
