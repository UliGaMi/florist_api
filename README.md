# Florist API

## Descripción

Florist API es una API RESTful desarrollada con [FastAPI](https://fastapi.tiangolo.com/) para gestionar productos y órdenes en una floristería. La API interactúa con una base de datos MySQL para almacenar productos y pedidos. Se puede configurar la base de datos proporcionando una URL de conexión en un archivo `.env` en la raíz del proyecto.

## Requisitos

- Python 3.9 o superior
- MySQL 8.0 o superior
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (opcional, pero recomendado)

## Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu_usuario/florist_api.git
cd florist_api
```

### 2. Configurar un Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la Base de Datos
Asegúrate de tener una base de datos MySQL configurada. Debes crear una base de datos, un usuario y otorgarle permisos.
Crea un archivo .env en la raíz del proyecto con la URL de conexión a la base de datos. La estructura general de la URL es:
```env
DATABASE_URL=mysql+asyncmy://usuario:contraseña@host:puerto/nombre_base_datos
```
Reemplaza usuario, contraseña, host, puerto, y nombre_base_datos con los valores correspondientes.

### 5. Iniciar la API
Para iniciar el servidor de desarrollo, utiliza Uvicorn:
```bash
uvicorn main:app --reload
```
El servidor debería estar disponible en http://127.0.0.1:8000.


