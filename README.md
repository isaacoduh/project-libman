# Library Management System

## Description

This is a **Library Management System** where users can browse, borrow, and return books. Administrators can manage books and users. The system uses JWT authentication for secure access to the API, and API documentation is available via Swagger.

### Features:
- **Anonymous Users**: Browse books but cannot borrow them.
- **Registered Users**: Can search for and borrow books.
- **Administrators**: Can add/remove books and manage users.
- **JWT Authentication**: Secure API endpoints.
- **API Documentation**: Automatically generated API documentation available at `/swagger/`.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Token)
- **Testing**: Pytest
- **API Documentation**: DRF-YASG
- **Containerization**: Docker, Docker Compose
- **Deployment**: DigitalOcean Droplet

## Prerequisites
- **Python 3.x**
- **PostgreSQL** (if running locally)
- **Docker** and **Docker Compose** (for containerization)
- **Git**


## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/isaacoduh/project-libman.git
cd project-libman
```

### 2. Build and Set Up Docker

Ensure that **Docker** and **Docker Compose** are installed. If they are not, follow the installation instructions for your system.

### 3. Build the Containers

To build the containers and set up the application, run the following command:

```bash
docker compose -f docker-compose.yml up --build -d --remove-orphans
```

This will:
- Build the **API** container using the `Dockerfile`.
- Start the **API** and **PostgreSQL** containers.
- Bind ports `8000` for the API and `5432` for PostgreSQL.

### 4. Configure the Database

Make sure that the database connection URL (`DATABASE_URL`) in the `docker-compose.yml` file points to the correct values:

```yaml
environment:
  - DEBUG=1
  - SECRET_KEY=XXXXXXX
  - DATABASE_URL=postgres://<username>:<password>@<host>:5432/dbname
```

### 5. Run Database Migrations

Run migrations to set up the database schema:

```bash
docker compose -f docker-compose.yml run --rm api python manage.py migrate
```

### 6. Create a Superuser

To access the Django admin panel, create a superuser account:

```bash
docker compose -f docker-compose.yml run --rm api python manage.py createsuperuser
```

Follow the prompts to set up the superuser.

### 7. Run the Application

Once the setup is complete, start the application:

```bash
docker compose -f docker-compose.yml up -d
```

You can now access your application at `http://127.0.0.1:8000/`.

### 8. Access the Swagger Documentation

The API documentation is available at:

[http://144.126.199.233:8000/swagger/](http://144.126.199.233:8000/swagger/)

## Testing

To run tests for the project, execute the following:

```bash
docker compose -f docker-compose.yml run --rm api python -m pytest tests/
```

## Deployment

### Deploying to DigitalOcean

1. **Create a Droplet** on DigitalOcean with Docker installed. You can follow their [tutorial on setting up Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04).
   
2. **SSH into your droplet**:
   ```bash
   ssh root@your_droplet_ip
   ```

3. **Clone the Repository on the Droplet**:
   ```bash
   git clone https://github.com/isaacoduh/project-libman.git
   cd project-libman
   ```

4. **Install Docker and Docker Compose** on the droplet (if not already installed).

5. **Build and Start the Containers**:
   ```bash
   docker compose -f docker-compose.yml up --build -d --remove-orphans
   ```

6. **Check the Application** by navigating to your Droplet's IP on port 8000:
   ```bash
   http://<your_droplet_ip>:8000/
   ```

### Notes:
- If deploying on a DigitalOcean Droplet, make sure the necessary ports (e.g., `8000`, `5432`) are open in your firewall settings.

## Docker Commands

- **Build Containers**:
  ```bash
  docker compose -f docker-compose.yml up --build -d --remove-orphans
  ```

- **Start Containers**:
  ```bash
  docker compose -f docker-compose.yml up -d
  ```

- **Stop Containers**:
  ```bash
  docker compose -f docker-compose.yml down
  ```

- **Run Migrations**:
  ```bash
  docker compose -f docker-compose.yml run --rm api python manage.py migrate
  ```

- **Run Tests**:
  ```bash
  docker compose -f docker-compose.yml run --rm api python -m pytest tests/
  ```

## API Endpoints

- **GET /api/books/**: List all books.
- **POST /api/borrow/**: Borrow a book (only available to registered users).
- **POST /api/return/**: Return a borrowed book.
- **Admin Panel**: `/admin/` for managing users and books.

## Security Considerations

- **CSRF Protection**: The application is secured against CSRF attacks.
- **SQL Injection**: The application uses Django's ORM, which prevents SQL injection.
- **XSS Protection**: All user inputs are sanitized to prevent XSS attacks.

## Contributing

Feel free to fork the repository and submit pull requests. If you find any issues or have suggestions for improvement, please create an issue on the GitHub repository.

---

## Links

- **Swagger Documentation**: [http://144.126.199.233:8000/swagger/](http://144.126.199.233:8000/swagger/)

---
