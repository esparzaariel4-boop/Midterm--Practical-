# Midterm - Practical

Implementación de una API REST con FastAPI y SQLModel que aplica técnicas criptográficas modernas para proteger las credenciales de los usuarios mediante Hashing, Salting y Peppering.

## Objetivo

Desarrollar un sistema de autenticación seguro que proteja las contraseñas de los usuarios aplicando tres capas de seguridad:

- **Hashing** con bcrypt para almacenar contraseñas de forma irreversible
- **Salting** automático por usuario para evitar ataques de tablas arcoíris
- **Peppering** mediante variables de entorno para proteger las credenciales incluso si la base de datos es comprometida

## Requisitos

- Python 3.12+
- WSL o Linux

## Instalación

**1. Clona el repositorio:**
```bash
git clone https://github.com/esparzaariel4-boop/Informe-del-proyecto.git
cd Informe-del-proyecto
```

**2. Crea y activa el entorno virtual:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instala las dependencias:**
```bash
pip install -r requirements.txt
```

**4. Crea el archivo `.env` con tu pepper:**
```bash
PEPPER=tuClaveSecretaAqui
```

**5. Levanta el servidor:**
```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/register` | Registra un nuevo usuario |
| POST | `/login` | Autentica un usuario existente |

## Ejemplo de ejecución

**Registrar un usuario:**
```json
POST /register
{
  "username": "ariel",
  "password": "mi123"
}
```
Respuesta:
```json
{
  "message": "Usuario registrado exitosamente"
}
```

**Iniciar sesión:**
```json
POST /login
{
  "username": "ariel",
  "password": "mi123"
}
```
Respuesta:
```json
{
  "message": "Inicio de sesión exitoso"
}
```

Puedes probar los endpoints directamente desde la documentación interactiva en `http://127.0.0.1:8000/docs`

## Tecnologías utilizadas

- FastAPI
- SQLModel
- SQLite
- bcrypt
- python-dotenv
- uvicorn
