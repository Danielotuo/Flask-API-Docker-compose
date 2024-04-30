# Flask REST API with PostgreSQL and Docker Compose

This case study is a Flask REST API that communicates with a PostgreSQL database using SQLAlchemy. The application is containerized using Docker Compose.
The case study uses the Application Factory pattern, Blueprints, and Docker secrets for securely storing sensitive information.

## Project Structure

The case-study follows this structure:

```
case-study/
├── app/
│ ├── __init__.py
│ ├── routes.py
│ └── models.py
├── secrets/
│ └── db_password.txt
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── .dockerignore

```

- `app/`: Contains the Flask application code.
  - `__init__.py`: Sets up the Flask application and database connection.
  - `routes.py`: Defines the API routes and view functions.
  - `models.py`: Defines the database model using SQLAlchemy.
- `secrets/`: Contains the secret file.
  - `db_password.txt`: Stores the database password as a secret.
- `Dockerfile`: Defines the Docker image for the Flask application.
- `docker-compose.yml`: Defines the services and their configurations with default network
- `requirements.txt`: Lists the Python dependencies for the application.
- `.gitignore`: Specifies files (secrets) and directories to be ignored by Git.
- `.dockerignore`: Specifies files and directories (README.md, secrets/, .gitignore) to be ignored by Docker.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

```
git clone https://github.com/Danielotuo/Flask-API-Docker-compose.git
```

2. Navigate to the project directory:

```
cd your-repo
```

3. Create the `secrets/db_password.txt` file and add a database password. Create a .dockerignore file and add the README.md, .gitignore and secrets directory to it.

4. Build and start the application using Docker Compose:

```
docker compose up -d
```

This command will build the Docker images and start the containers in detached mode.

5. Create the database tables:

- Open a new terminal and execute the following command to start a Flask shell within the `flask_app` container:
  ```
  docker compose exec flask_app flask shell
  ```
- Inside the Flask shell, run the following commands to create the database tables:
  ```python
  from app import db
  db.create_all()
  ```
- Exit the Flask shell with `exit()` or `Ctrl+D`.

6. Access the API at `http://localhost:5000` in the browser.

## Testing the API

Here are examples of how to use curl to test the API endpoints:

- Add a new product:

```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Product", "price": 5.99}' http://localhost:5000/products
```

- Retrieve all products:

```
curl http://localhost:5000/products
```

- Retrieve a specific product by ID<>:

```
curl http://localhost:5000/products/1
```

## Stopping the containers for the services

To stop and remove containers, run the following command:

```
docker compose down
```

## Application Factory and Blueprints

This case study uses the Application Factory pattern and Blueprints for better code organization and modularity instead of a single flask `app.py` file.

- The Application Factory pattern is implemented in `app/__init__.py`.

- Blueprints are used in `app/routes.py` to define the API routes.

## Secrets Management

The project uses Docker secrets to store the database password. The `secrets/db_password.txt` file contains the database password, which is mounted as a secret file inside the containers.

## Conclusion

This README provides an overview of how to deploy a simple application using Docker Compose, consisting of two services: a REST API and a PostgreSQL database, with instructions on how to build and start the application, and examples of curl requests to test the API.

To go further, additional features can be added such as pytest for testing, data validation, more API endpoints, error handling, use migration tools like Flask-Migrate to manage database schema changes instead of using Flask shell to run the db.create_all() command, CI/CD etc. The case study can be extended to include frontend components, such as a React app as well.
