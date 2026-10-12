## 👥 Autor
* [Christian Cañar]
---
# Seminario de Integración - Proyecto Final

Repositorio oficial para el desarrollo del proyecto de la materia **Seminario de Integración**. Este sistema implementa una arquitectura moderna de tipo Full Stack, separando el Back-end (API de alto rendimiento) y el Front-end (Interfaz de usuario escalable).

---

## 🚀 Tecnologías Principales y Mini Conceptos

### 1. FastAPI (Back-end)
* **¿Qué es?** Es un framework web moderno y de alto rendimiento para construir APIs con **Python 3.8+**, basado en las anotaciones de tipos estándar de Python.
* **Características clave:**
  * **Velocidad extrema:** Su rendimiento está a la par de NodeJS y Go gracias a Starlette y Pydantic.
  * **Documentación automática:** Genera de forma interactiva la documentación de la API mediante Swagger UI y ReDoc sin configuración extra.
  * **Validación de datos:** Aprovecha los modelos de Pydantic para asegurar que los datos de entrada y salida cumplan estrictamente con los tipos definidos.

### 2. TypeScript (Lenguaje del Front-end)
* **¿Qué es?** Es un superconjunto de JavaScript de código abierto que añade **tipado estático opcional** y características avanzadas al lenguaje.
* **Características clave:**
  * **Detección temprana de errores:** Permite identificar fallos de tipos e inconsistencias directamente en el editor antes de compilar o ejecutar el código.
  * **Escalabilidad:** Facilita la refactorización y el mantenimiento en aplicaciones grandes y complejos equipos de desarrollo.
  * **Orientación a objetos:** Soporta clases, interfaces, genéricos y módulos de manera robusta.

### 3. Angular (Front-end)
* **¿Qué es?** Es un framework de desarrollo front-end basado en componentes, mantenido por Google y desarrollado completamente en **TypeScript**, ideal para aplicaciones web de una sola página (SPA).
* **Características clave:**
  * **Arquitectura modular y basada en componentes:** Permite dividir la interfaz en piezas reutilizables, independientes y altamente organizadas.
  * **Inyección de dependencias:** Cuenta con un sistema interno que facilita la gestión y prueba de servicios y componentes.
  * **Herramientas integradas:** Provee un ecosistema completo para enrutamiento (`Router`), peticiones HTTP (`HttpClient`) y formularios reactivos de serie.

---

## 📂 Estructura del Repositorio

La estructura del proyecto se organiza separando claramente el servidor y la interfaz de usuario:

```text
/
├── backend/          # Código fuente de FastAPI (Python + uv)
├── frontend/         # Aplicación de Angular (TypeScript)
└── README.md         # Documentación general del proyecto
```

---

## 🛠️ Guía de Inicio Rápido

### Prerrequisitos
Asegúrate de tener instalado en tu sistema:
* **Python** (versión 3.10 o superior) y el gestor de entornos **`uv`**
* **Node.js** y **npm** (o un gestor equivalente)
* **Angular CLI**

### 1. Configurar y ejecutar el Back-end (FastAPI)
```bash
# Entrar a la carpeta del backend
cd backend

# Crear el entorno virtual con uv e instalar dependencias
uv venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Ejecutar el servidor de desarrollo
fastapi dev main.py
```

### 2. Configurar y ejecutar el Front-end (Angular)
```bash
# Entrar a la carpeta del frontend
cd frontend

# Instalar dependencias de Node.js
npm install

# Iniciar la aplicación de Angular
ng serve
```