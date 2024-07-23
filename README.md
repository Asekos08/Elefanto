# Book Project

## Overview

This is a Django project for managing books, genres, authors, reviews, and user favorites. The project includes endpoints for book management, user authentication, and review handling.

## Getting Started

To set up and run this project locally, follow these steps:

### 1. Clone the Repository

First, clone the repository to your local machine, then access the bookproject folder

### 2.  Install Dependencies

Ensure you have Python installed, then install the required Python packages:

```bash
pip install -r requirements.txt
```
### 3. Set Up Environment Variables
Create a .env file in the project root directory and add your Django secret key:

```bash
SECRET_KEY=your_secret_key_here
```

### 4. Run Migrations
Create and apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server
Run the development server:
```bash
python manage.py runserver
```

### 6. Access the API Documentation
The project includes Swagger documentation for the API endpoints. You can access it at:
```bash
http://127.0.0.1:8000/swagger/
```



