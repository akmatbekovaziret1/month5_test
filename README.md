# Blog REST API

Simple blog REST API built with Django REST Framework and PostgreSQL.

## Installation

Clone the repository:

```bash
git clone https://github.com/akmatbekovaziret1/month5_test.git
cd month5_test/blog
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your PostgreSQL database in `settings.py`.

Apply migrations:

```bash
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

## Features

* User registration and token authentication
* CRUD for posts and comments
* Author-based permissions
* Post and comment visibility
* Pagination
* PostgreSQL
