# Movie Web Application

## Description

This project is a web application developed with the Django framework that allows users to view and edit a list of
movies. It features models with relationships to represent movies, directors, and actors. The application provides
functionalities to create, update, and delete movie records through both Django's base view classes and the Django REST
Framework.

### Features

- **Movie Details**: Each movie record includes title, release year, director, runtime, poster and a list of actors.
- **Model Relationships**: Developed with thoughtful consideration on how to best represent the relationships between
  movies, actors, and directors.
- **Initial Database Population**: Uses the API from https://www.omdbapi.com/ to initially fill the database with movie
  records.
- **CRUD Operations**: Supports creating, reading, updating, and deleting records using Django's view classes and the
  Django REST Framework.
- **Pagination**: Implements pagination for long lists, showing 25 records per page.
- **Filtering**: Allows filtering movies by year, director, and actor using django-filters.
- **Hosting**: The site is hosted, providing access to the web application.

## Installation

### Cloning the Repository

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/OlegatorLE/bond_movie_api
    cd bond_movie_api
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Migrate the database:
    ```bash
    python manage.py migrate
    ```
4. Add your SECRET_KEY and OMDb_API_KEY to .env

5. Populate the database using the script (optional):
    ```bash
    python fill_database.py
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

### Using Docker

1. Ensure Docker is installed on your machine.
2. Build the Docker image:
    ```bash
    docker build -t bond_movie_api .
    ```
3. Run the application in a Docker container:
    ```bash
    docker run -d -p 8000:8000 bond_movie_api
    ```

## Usage

Navigate to `http://localhost:8000/` in your web browser to access the movie catalogue application. From there, you can
browse the list of movies, add new movies, edit existing records, or delete them.