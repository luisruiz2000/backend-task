# Backend - Prueba Técnica

Este proyecto implementa una API RESTful para la gestión de tareas utilizando **FastAPI**.

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

1. Clona el repositorio y navega al directorio del backend:

   ```sh
   cd backend
   ```

2. Instala las dependencias:
   ```sh
   pip install -r requeriments.txt
   ```

## Ejecución del servidor de desarrollo

```sh
uvicorn main:app --reload
```

El servidor estará disponible en: [http://localhost:8000](http://localhost:8000)

## Endpoints disponibles

- **GET /tasks**  
  Devuelve una lista de todas las tareas.

- **POST /tasks**  
  Crea una nueva tarea.  
  Cuerpo esperado (JSON):

  ```json
  {
    "title": "Título de la tarea",
    "description": "Descripción de la tarea"
  }
  ```

- **PUT /tasks/{task_id}?completed=true/false**  
  Actualiza el estado `completed` de una tarea.

- **DELETE /tasks/{task_id}**  
  Elimina una tarea específica.

## Manejo de errores

- Si se solicita un `task_id` que no existe, la API responde con un **404 Not Found** y un mensaje adecuado.

## Documentación automática

FastAPI genera documentación interactiva en:

- [Swagger UI](http://localhost:8000/docs)
- [ReDoc](http://localhost:8000/redoc)
