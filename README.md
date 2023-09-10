# Django REST Blog API

## Introduction
This project provides a RESTful API for a simple blog application. The API allows you to manage users, posts, comments, and categories. It's built using Django and Django REST Framework and is designed for those looking to integrate a blog feature into their existing project or create a backend service for a blog.

## Features
User Management: Create, read, update, and delete (CRUD) operations for users.
Post Management: CRUD operations for blog posts.
Comment Management: CRUD operations for comments on blog posts.
Category Management: CRUD operations for post categories.
Authentication: Secure API endpoints with token-based authentication.

## Installation and Setup

1. Clone the Repository

```
git clone https://github.com/yourusername/django-rest-blog-api.git
cd django-rest-blog-api
```

2. Set up a Virtual Environment

```
python3 -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
```

3. Install Dependencies

```
pip install -r requirements.txt
```

4. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

5. Run the Development Server

```
python manage.py runserver
```

6. API Endpoints

- List all users: GET /users/
- User details: GET /users/<int:pk>
- List all posts: GET /posts/
- Post details: GET /posts/<int:pk>

## Technology Stack

- Programming Language: Python 3.10
- Web Framework: Django 4.2.5
- REST Framework: Django REST Framework
- Database: SQLite (default)

## Contributions
Feel free to submit pull requests, create issues or spread the word.

## License
MIT License


