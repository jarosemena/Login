# Login
General Login to use like a microservice for all the environment

---

# Proyecto de Aplicación de Login

## 1. Descripción del Proyecto

Este proyecto es una aplicación de login que permite la creación de usuarios, recuperación de contraseñas y autenticación a través de servicios de terceros como Google, Facebook y Outlook. La aplicación está dividida en dos partes: un backend desarrollado en Flask y un frontend en React utilizando Material-UI.

## 2. Estructura del Proyecto
/mi-proyecto
│
├── /backend
│   ├── /app
│   │   ├── /models          # Modelos de datos
│   │   ├── /services        # Lógica de negocio
│   │   ├── /controllers     # Controladores para manejar las solicitudes
│   │   ├── /repositories     # Acceso a datos
│   │   ├── /routes          # Rutas de la API
│   │   ├── /utils           # Funciones utilitarias
│   │   └── /tests           # Pruebas unitarias
│   │
│   ├── /migrations          # Migraciones de la base de datos
│   ├── /requirements.txt    # Dependencias de Python
│   └── app.py               # Archivo principal de la aplicación
│
└── /frontend
    ├── /src
    │   ├── /components      # Componentes de React
    │   ├── /pages           # Páginas de la aplicación
    │   ├── /services        # Servicios para hacer llamadas a la API
    │   ├── /utils           # Funciones utilitarias
    │   └── index.js         # Archivo principal de React
    │
    ├── package.json          # Dependencias de React
    └── .env                  # Variables de entorno
## 3. Funcionalidades

- **Registro de nuevos usuarios**: Permite a los usuarios registrarse mediante un formulario o autenticarse a través de servicios de terceros (Google, Facebook, Outlook).
- **Inicio de sesión**: Los usuarios pueden iniciar sesión si ya están registrados.
- **Recuperación de contraseña**: Los usuarios pueden recuperar su contraseña mediante un código enviado por correo electrónico.
- **Autenticación JWT**: Se genera un token JWT para las sesiones de usuario.
- **Seguridad**: Implementación de medidas de seguridad para prevenir ataques comunes como inyecciones SQL y ataques de fuerza bruta.

## 4. Tecnologías Utilizadas

- **Backend**:
  - Flask
  - Flask-SQLAlchemy
  - Flask-Migrate
  - Flask-JWT-Extended
  - Flask-Mail
  - MySQL
  - Flask-WTF
  - Flask-Limiter
  - bcrypt
  - pytest

- **Frontend**:
  - React
  - Redux
  - Material-UI
  - Jest
  - React Testing Library

## 5. Instalación

### Backend

1. Clona el repositorio:
git clone https://github.com/tu-usuario/mi-proyecto.git
   cd mi-proyecto/backend
2. Crea un entorno virtual y actívalo:
python -m venv venv
   venv\Scripts\activate  # En Windows
   # source venv/bin/activate  # En macOS/Linux
3. Instala las dependencias:
pip install -r requirements.txt
4. Configura la base de datos MySQL y actualiza  `app.py`  con tus credenciales.

5. Ejecuta la aplicación:
python app.py
### Frontend

1. Navega a la carpeta del frontend:
cd ../frontend
2. Instala las dependencias:
npm install
3. Ejecuta la aplicación:
npm start
## 6. Pruebas

Para ejecutar las pruebas en el backend, asegúrate de que el entorno virtual esté activado y ejecuta:
pytest
Para ejecutar las pruebas en el frontend, navega a la carpeta del frontend y ejecuta:
npm test
## 7. Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## 8. Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

---

## 9. Comandos para Crear la Estructura del Proyecto en Windows

### Crear la Estructura del Proyecto

1. **Crea el directorio principal del proyecto**:
mkdir mi-proyecto
   cd mi-proyecto
2. **Crea la carpeta para el backend**:
mkdir backend
   cd backend
3. **Crea la estructura del backend**:
mkdir app
   cd app
   mkdir models services controllers repositories routes utils tests
   cd ..
   mkdir migrations
   echo. > requirements.txt
   echo. > app.py
   cd ..
4. **Crea la carpeta para el frontend**:
mkdir frontend
   cd frontend
5. **Crea la estructura del frontend**:
mkdir src
   cd src
   mkdir components pages services utils
   echo. > index.js
   cd ..
   echo. > package.json
   echo. > .env
   cd ..
---

