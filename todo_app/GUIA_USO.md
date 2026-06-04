# Guía de Uso - Aplicación To-Do List

## 🎬 Cómo Empezar

### 1. Inicia la Aplicación
```bash
python run.py
```

### 2. Accede a la URL
```
http://localhost:5000
```

### 3. Navega a la Sección de Tareas
```
http://localhost:5000/tareas/
```

---

## 💼 Casos de Uso

### Caso 1: Crear una Nueva Tarea

1. Ve a `http://localhost:5000/tareas/`
2. En el campo "Escribe tu nueva tarea aquí...", ingresa una tarea
3. Ejemplo: "Comprar leche"
4. Haz clic en el botón "+ Agregar Tarea"
5. ✅ La tarea aparecerá en la lista

**Notas:**
- El título es obligatorio
- Se recortan espacios en blanco
- Máximo 200 caracteres

---

### Caso 2: Marcar una Tarea como Completada

**Opción A: Usando el Checkbox**
1. Haz clic en el checkbox a la izquierda de la tarea
2. La tarea se mostrará tachada (gris)
3. Vuelve a hacer clic para desmarcar

**Opción B: Usando el Botón**
1. Haz clic en el botón "✓ Completar"
2. El botón cambia a "↶ Deshacer"
3. Haz clic nuevamente para marcar como incompleta

**Cambios visuales:**
- Fondo: Blanco → Verde claro
- Texto: Negro → Gris tachado
- Botón: Verde → Gris

---

### Caso 3: Eliminar una Tarea

1. Busca la tarea que deseas eliminar
2. Haz clic en el botón "🗑️ Eliminar" (ícono de basura)
3. Se abrirá un cuadro de confirmación: "¿Estás seguro de que deseas eliminar esta tarea?"
4. Haz clic en "OK" para confirmar o "Cancelar" para desistir
5. ✅ La tarea será eliminada

---

## 📊 Interpretación de la Interfaz

### Estadísticas

```
┌─────────────────────┬──────────────────┐
│  Total de Tareas    │   Completadas    │
│        5            │        2         │
└─────────────────────┴──────────────────┘
```

- **Total de Tareas:** Número total de tareas en la lista
- **Completadas:** Número de tareas marcadas como completadas

### Tareas Incompletas

```
┌─ ☐ Comprar leche ─────────────────────┬──────┬──────────┐
│                                        │ ✓    │ 🗑️       │
│                                        │Compl │ Eliminar │
└────────────────────────────────────────┴──────┴──────────┘
```

### Tareas Completadas

```
┌─ ☑ Hacer la cama ────────────────────┬──────┬──────────┐
│ (tachado, gris)                      │ ↶    │ 🗑️       │
│                                       │Desha │ Eliminar │
└───────────────────────────────────────┴──────┴──────────┘
```

---

## ⌨️ Atajos de Teclado

| Acción | Atajo |
|--------|-------|
| Ir al campo de entrada | `Alt + T` (algunos navegadores) |
| Enviar formulario | `Enter` (cuando el foco está en el campo) |
| Navegar entre elementos | `Tab` |
| Navegar atrás | `Shift + Tab` |

---

## 🎯 Consejos Útiles

### ✅ Buenas Prácticas

1. **Sé específico en los títulos**
   - ❌ "Cosas"
   - ✅ "Comprar leche, pan y huevos en el supermercado"

2. **Completa tareas regularmente**
   - Mantén la lista limpia
   - Satisfacción visual de avance

3. **Usa títulos cortos y concisos**
   - ❌ "Necesito ir al correo para enviar el paquete que dejé ayer en casa"
   - ✅ "Enviar paquete por correo"

### 🎨 Características Visuales

- **Color gradient:** Fondo con gradiente morado (profesional)
- **Animaciones:** Las tareas tienen entrada suave
- **Iconos:** Font Awesome para mejor UX
- **Responsive:** Se adapta a cualquier tamaño de pantalla

---

## 📱 Uso en Dispositivos Móviles

### Pantalla Móvil (< 576px)

- Botones compactos
- Solo iconos visibles
- Títulos más cortos
- Optimizado para touch

### Pantalla Tablet (576px - 992px)

- Botones con texto e iconos
- Interfaz equilibrada
- Buen espacio para interactuar

### Pantalla Desktop (> 992px)

- Interfaz completa
- Máximo ancho de 600px para mantener legibilidad
- Centrada en la pantalla

---

## 🔍 Ejemplos de Listas de Tareas

### Ejemplo 1: Tareas Personales

```
☐ Hacer ejercicio (30 minutos)
☐ Leer un capítulo del libro
☑ Tomar desayuno
☐ Llamar a mamá
☑ Ducharme
☐ Preparar la cena
```

### Ejemplo 2: Tareas de Trabajo

```
☐ Responder emails del proyecto X
☑ Presentación a las 3 PM
☐ Revisar código del PR #123
☐ Actualizar documentación
☑ Reunión con el equipo
☐ Hacer backup de los archivos
```

### Ejemplo 3: Tareas de Proyecto

```
☐ Diseñar interfaz
☐ Implementar CRUD
☑ Testing básico
☐ Optimizar rendimiento
☐ Escribir documentación
☐ Deploy a producción
```

---

## 🆘 Preguntas Frecuentes

### P: ¿Mis tareas se guardan?
**R:** No, las tareas se almacenan en memoria. Si cierras la pestaña o reinicas la aplicación, se pierden. Para guardar permanentemente, necesitarás una base de datos.

### P: ¿Puedo editar una tarea?
**R:** Actualmente no hay función de edición. Debes eliminarla y crear una nueva. Esto se puede agregar como mejora futura.

### P: ¿Hay límite de tareas?
**R:** No hay límite técnico, pero la interfaz puede volverse lenta con muchas tareas (1000+).

### P: ¿Puedo compartir mis tareas?
**R:** No con esta versión. Esto requeriría autenticación y base de datos.

### P: ¿Funciona sin internet?
**R:** Parcialmente. La aplicación local funciona, pero los estilos de Bootstrap vienen del CDN, así que necesitas internet para verlos correctamente.

---

## 📞 Reporte de Problemas

Si encuentras algún problema:

1. Describe qué esperabas
2. Describe qué sucedió
3. Proporciona pasos para reproducir
4. Captura pantallas si es posible
5. Abre un issue en GitHub

**Ejemplo:**
```
Título: El botón de eliminar no funciona

Descripción:
- Esperaba: Eliminar la tarea al hacer clic
- Sucedió: La página se recarga pero la tarea sigue ahí
- Pasos: Crea una tarea → Haz clic en Eliminar → Cancela
- Navegador: Chrome en Windows 11
```

---

**¡Disfruta tu experiencia con To-Do List!** 🚀
