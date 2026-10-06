# 🔐 Secure Backend API

A secure RESTful backend application built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **JWT/OAuth2 authentication**, **role-based access control (RBAC)**, **file uploads**, **logging**, **automated testing**, and **Docker**.

This project demonstrates how to build, secure, test, and containerize a production-style Python backend.

---

## 🚀 Features

- 🔐 JWT-based authentication
- 🔑 OAuth2 Password Bearer authentication
- 👤 User registration and login
- 🔒 Protected API endpoints
- 🛡️ Role-Based Access Control (RBAC)
- 🔑 Secure password hashing with bcrypt
- 🗄️ PostgreSQL database
- 🧩 SQLAlchemy ORM
- 📁 Secure file upload with file type and size validation
- 📝 Application logging
- 🧪 Automated API testing with Pytest
- 📚 Interactive Swagger/OpenAPI documentation
- 🐳 Docker and Docker Compose support
- ❤️ Health-check endpoint
- 🌐 CORS configuration
- 🔒 Environment-based configuration

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.13 | Backend development |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM and database operations |
| Psycopg2 | PostgreSQL connectivity |
| JWT | Authentication tokens |
| OAuth2 | Authentication flow |
| Passlib | Password hashing |
| Bcrypt | Secure password hashing |
| Pydantic | Data validation |
| Pytest | Automated testing |
| Uvicorn | ASGI server |
| Docker | Containerization |
| Docker Compose | Multi-container application |
| Git | Version control |
| GitHub | Project hosting |

---

## 📁 Project Structure

```text
secure_backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── logger.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── files.py
│   │
│   └── uploads/
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api.py
│
├── logs/
│
├── .env
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🔐 Authentication Flow

```text
User Registration
       ↓
Password Hashing
       ↓
PostgreSQL
       ↓
User Login
       ↓
Password Verification
       ↓
JWT Token Generated
       ↓
Bearer Token
       ↓
Protected API
```

---

## 👥 RBAC

The application supports role-based access control.

### User

A normal user can:

- View their own profile
- Upload files
- Access authenticated endpoints

### Admin

An administrator can:

- View users
- Access admin-protected endpoints
- Perform administrative operations

Protected endpoints use FastAPI dependencies to validate the JWT and user role.

---

## 📌 API Endpoints

### General

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| GET | `/` | API root | No |
| GET | `/health` | Health check | No |

### Authentication

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/auth/register` | Register a user | No |
| POST | `/auth/login` | Login and generate JWT | No |

### Users

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| GET | `/users/me` | Get current user profile | JWT |
| GET | `/users/` | Get all users | Admin |

### File Upload

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/files/upload` | Upload a file | JWT |

---

## ⚙️ Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/secure_backend.git
cd secure_backend
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

CMD:

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ PostgreSQL Setup

Create the PostgreSQL database:

```sql
CREATE DATABASE secure_db;
```

Default local configuration used by this project:

```text
Host: localhost
Port: 5432
Username: postgres
Database: secure_db
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/secure_db

SECRET_KEY=YOUR_GENERATED_SECRET_KEY
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Generate a secure JWT secret key with Python:

```bash
python -c "import secrets; print(secrets.token_urlsafe(64))"
```

Copy the generated value into:

```env
SECRET_KEY=your-generated-key
```

⚠️ **Never commit `.env` to GitHub.**

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 Swagger API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger provides an interactive interface for:

- Registration
- Login
- JWT authorization
- Protected endpoints
- RBAC testing
- File uploads

---

## 🔑 Login and JWT Authentication

### Register

```http
POST /auth/register
```

Request:

```json
{
  "username": "harshith",
  "email": "harshith@gmail.com",
  "password": "Password@123"
}
```

### Login

Use the Swagger OAuth2 authorization flow or send credentials to:

```http
POST /auth/login
```

The API returns:

```json
{
  "access_token": "YOUR_JWT_TOKEN",
  "token_type": "bearer"
}
```

### Authorize Swagger

Click:

```text
Authorize 🔒
```

Enter your username and password.

Swagger will obtain the JWT token and use it for protected endpoints.

---

## 🔒 Protected API Example

Request:

```http
GET /users/me
Authorization: Bearer YOUR_JWT_TOKEN
```

Example response:

```json
{
  "id": 1,
  "username": "harshith",
  "email": "harshith@gmail.com",
  "role": "user"
}
```

---

## 📁 File Upload

Endpoint:

```http
POST /files/upload
```

Supported file types:

```text
.jpg
.jpeg
.png
.pdf
.txt
```

Maximum file size:

```text
5 MB
```

Uploaded files are stored in:

```text
app/uploads/
```

Files receive generated unique filenames to avoid filename collisions.

---

## 📝 Logging

Application logs are stored in:

```text
logs/app.log
```

The application logs important events such as:

- User registration
- Successful login
- Failed authentication attempts
- API requests
- API response status
- File uploads

---

## 🧪 Testing

Run all tests:

```bash
python -m pytest -v
```

Current test coverage includes:

- Root endpoint
- Health endpoint
- Unauthorized access to protected endpoints

Example result:

```text
tests/test_api.py::test_root PASSED
tests/test_api.py::test_health PASSED
tests/test_api.py::test_protected_route_without_token PASSED

3 passed
```

---

## 🐳 Dockerization

The project includes:

- `Dockerfile`
- `docker-compose.yml`
- PostgreSQL container
- FastAPI backend container
- Persistent PostgreSQL volume
- Upload and log volume mappings

### Prerequisites

Install Docker Desktop:

https://www.docker.com/products/docker-desktop/

Docker Desktop should be running before executing Docker commands.

For Windows, Docker Desktop can use the WSL 2 backend.

### Build the containers

```bash
docker compose build
```

### Start the application

```bash
docker compose up -d
```

### Check containers

```bash
docker compose ps
```

Expected services:

```text
secure_backend
secure_postgres
```

### View backend logs

```bash
docker compose logs backend
```

### Follow backend logs

```bash
docker compose logs -f backend
```

### Stop containers

```bash
docker compose down
```

### Stop containers and remove database volume

```bash
docker compose down -v
```

⚠️ `docker compose down -v` removes the PostgreSQL Docker volume and therefore deletes the database data stored in that volume.

---

## 🐘 Docker PostgreSQL Connection

When running locally:

```text
postgresql+psycopg2://postgres:PASSWORD@localhost:5432/secure_db
```

When the backend runs inside Docker Compose, it connects to PostgreSQL using the service name:

```text
postgresql+psycopg2://postgres:admin@db:5432/secure_db
```

The Docker Compose service name `db` acts as the hostname between containers.

---

## 🩺 Health Check

Endpoint:

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

## 🔒 Security Practices

This project implements several basic backend security practices:

- Passwords are never stored as plain text.
- Passwords are hashed using bcrypt.
- JWT tokens are signed using a secret key.
- Protected routes require authentication.
- Admin routes verify the user's role.
- Uploaded files are restricted by extension.
- Uploaded files are limited to 5 MB.
- Environment variables are used for sensitive configuration.
- `.env` is excluded from Git.
- API activity is logged.

> For production deployment, additional controls such as HTTPS, strict CORS origins, refresh-token rotation, rate limiting, stronger file-content validation, secret management, database migrations, and centralized logging should be added.

---

## 🔄 Application Architecture

```text
                   Client / Swagger
                          │
                          ▼
                    FastAPI API
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
     Authentication     RBAC        File Upload
          │               │               │
          ▼               ▼               ▼
         JWT          Protected       Validation
                          │
                          ▼
                      SQLAlchemy
                          │
                          ▼
                     PostgreSQL
                          │
                          ▼
                    Application Logs
```

---

## 📦 Requirements

Example `requirements.txt`:

```text
fastapi
uvicorn[standard]
python-jose[cryptography]
passlib==1.7.4
bcrypt==4.0.1
python-multipart
python-dotenv
sqlalchemy
psycopg2-binary
pydantic[email]
pytest
httpx
```

---

## 🧹 Git Configuration

Recommended `.gitignore`:

```gitignore
venv/
__pycache__/
*.pyc
.env
.pytest_cache/
.git/
logs/
app/uploads/*
```

Do not upload:

```text
.env
venv/
*.db
logs/
uploaded files
```

---

## 🚀 GitHub Commands

Initialize Git:

```bash
git init
```

Set the main branch:

```bash
git branch -M main
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial secure backend implementation"
```

Add your GitHub repository:

```bash
git remote add origin https://github.com/YOUR_USERNAME/secure_backend.git
```

Push:

```bash
git push -u origin main
```

---

## 🎯 Project Objective

The objective of this project is to demonstrate a secure and maintainable backend architecture using modern Python technologies.

The project covers:

- REST API development
- Authentication
- Authorization
- RBAC
- Database integration
- Secure password storage
- JWT security
- File handling
- Logging
- Automated testing
- Docker containerization

---

## 👨‍💻 Author

**Bachina Sai Harshith**

GitHub:  
https://github.com/saiharshith123

LinkedIn:  
https://www.linkedin.com/in/bachina-sai-harshith-b06a50208/

---

## ⭐ Future Enhancements

- Refresh token implementation
- Email verification
- Password reset
- Rate limiting
- Redis integration
- Database migrations with Alembic
- HTTPS configuration
- Advanced file-content validation
- Admin dashboard
- API versioning
- CI/CD with GitHub Actions
- Production deployment
- Centralized monitoring and logging

---

## 📄 License

This project is intended for educational and portfolio purposes.
