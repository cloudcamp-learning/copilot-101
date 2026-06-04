"""Archivo de entrada principal de la aplicación Flask.

Este módulo inicia la aplicación Flask en modo desarrollo.
Para producción, utiliza un servidor WSGI como Gunicorn.
"""

from app import create_app

if __name__ == '__main__':
    app = create_app()
    # Ejecutar en modo desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)
