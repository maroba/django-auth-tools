# django-auth-tools

Some tools for authentication in Django projects

## Installation

```bash
pip install django-auth-tools
```

Or for development:

```bash
git clone <your-repo-url>
cd django-auth-tools
pip install -e .
```

## Quick Start

1. Add `django_auth_tools` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "django_auth_tools",
]
```

2. Include the URLconf in your project `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    ...
    path("django_auth_tools/", include("django_auth_tools.urls")),
]
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

## Development

### Using the Sample Project

A sample Django project is included for development and testing:

```bash
cd sample_project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Running Tests

```bash
pip install tox
tox
```

## License

MIT
