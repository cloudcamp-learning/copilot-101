# paso 1
Actúa como un Arquitecto de Software Senior experto en Python y Flask. 
Quiero crear una aplicación web de lista de tareas (To-Do List) utilizando Flask. Para seguir las buenas prácticas de desarrollo, la aplicación debe estar estructurada utilizando Blueprints para separar la lógica de la aplicación del punto de entrada principal. El almacenamiento de las tareas debe ser un CRUD básico en memoria (usando una lista o diccionario global).

Por ahora, NO escribas la lógica interna de las funciones ni las plantillas HTML. Genera únicamente:
1. La estructura de carpetas y archivos recomendada (incluyendo carpetas para 'templates' y 'static').
2. El archivo 'run.py' o 'app.py' de entrada.
3. El archivo de inicialización del paquete (__init__.py) donde se configure la app de Flask y se registre un Blueprint llamado 'tareas'.
4. El archivo del Blueprint ('routes.py' o 'views.py') que contenga únicamente los comentarios de arquitectura, las rutas definidas (@tareas.route) y el esqueleto de las funciones con 'pass' para las siguientes operaciones:
   - Mostrar todas las tareas (GET /)
   - Crear una nueva tarea (POST /add)
   - Marcar una tarea como completada/incompleta (POST /toggle/<int:id>)
   - Eliminar una tarea (POST /delete/<int:id>)

Asegúrate de documentar con comentarios qué se espera en cada ruta antes de pasar al siguiente paso.

# paso 2
Actúa como un Desarrollador Flask Full Stack. 
Vamos a implementar la lógica completa del CRUD en memoria y la interfaz gráfica. Modifica el código anterior para cumplir con lo siguiente:

1. Lógica del Blueprint:
   - Define una estructura de datos para las tareas en memoria. Cada tarea debe tener: 'id' (autoincremental), 'titulo' (string) y 'completada' (booleano).
   - Implementa la lógica real para listar, añadir, cambiar estado (toggle) y eliminar tareas.
   - Después de añadir, editar o eliminar, redirige (redirect) al usuario a la vista principal.

2. Interfaz Gráfica (HTML + Jinja2):
   - Genera el código para un archivo 'base.html' (con la estructura general de HTML5 y soporte para que sea visualmente limpio, puedes sugerir clases de Bootstrap vía CDN).
   - Genera el código para 'index.html' que herede de 'base.html'. Este debe renderizar un formulario simple para añadir tareas y una lista/tabla que muestre las tareas actuales. Las tareas completadas deben mostrarse con un estilo diferente (por ejemplo, tachadas) y cada una debe tener sus botones para "Marcar como completada" y "Eliminar".

Presenta el código final refactorizado y listo para funcionar.

# paso 3
Actúa como un Ingeniero de QA / Tester Senior experto en Python. 
Quiero escribir pruebas unitarias para la aplicación Flask con Blueprints que acabamos de crear. Necesito que generes un archivo de pruebas llamado 'test_app.py' utilizando la librería nativa 'unittest' de Python y el cliente de pruebas de Flask (app.test_client()).

Las pruebas deben cubrir los siguientes escenarios:
1. 'test_index_route': Verificar que la página principal carga correctamente (Status 200) y que inicialmente muestra que no hay tareas (o el texto de la plantilla).
2. 'test_add_task': Verificar que enviar una nueva tarea mediante POST añade el elemento correctamente a la lista en memoria y redirige (Status 302).
3. 'test_toggle_task': Verificar que al cambiar el estado de una tarea existente, su propiedad 'completada' cambia de False a True.
4. 'test_delete_task': Verificar que al eliminar una tarea, esta desaparece del almacenamiento en memoria.

Asegúrate de incluir los métodos 'setUp' y 'tearDown' limpios para que cada prueba corra en un entorno aislado y la memoria se reinicie entre test y test. Explica brevemente cómo ejecutar los tests desde la terminal.
