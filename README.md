# Bakery Website

This is a Django project for a bakery website. It includes features for displaying bakery items, managing inventory, and providing an online presence for the bakery.

## Project Structure

```
bakery_website
├── bakery_website
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bakery
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates
│       └── bakery
│           └── index.html
├── manage.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd bakery_website
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install django
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Run the development server:**
   ```
   python manage.py runserver
   ```

6. **Access the website:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Features

- Display a list of bakery items.
- Admin interface for managing bakery items.
- Responsive design for mobile and desktop users.

## License

This project is licensed under the MIT License.