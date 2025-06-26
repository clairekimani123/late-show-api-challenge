# Late Show API Challenge

A RESTful API for managing episodes, guests, and appearances for a late show, built with Flask, SQLAlchemy, Flask-Migrate, and JWT authentication.

## Features

- User authentication with JWT
- CRUD operations for Episodes, Guests, and Appearances
- PostgreSQL database support
- Database migrations with Flask-Migrate
- Seed script for test data

## Project Structure

```
late-show-api-challenge/
├── server/
│   ├── app.py
│   ├── controllers/
│   ├── models/
│   └── seed.py
├── migrations/
├── config.py
├── Pipfile
└── README.md
```

## Setup

### 1. Clone the repository

```sh
git clone <repo-url>
cd late-show-api-challenge
```

### 2. Create and activate a virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure the database

Edit `config.py` to set your `SQLALCHEMY_DATABASE_URI`. Example for PostgreSQL:

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/late_show_db'
```

### 5. Run database migrations

```sh
export FLASK_APP=server.app
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Seed the database (optional)

```sh
python -m server.seed
```

### 7. Run the server

```sh
python -m server.app
```

The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- `POST /auth/register` — Register a new user
- `POST /auth/login` — Login and receive a JWT
- `GET /episodes/` — List episodes
- `POST /episodes/` — Create an episode
- `GET /guests/` — List guests
- `POST /guests/` — Create a guest
- `POST /appearances/` — Create an appearance

**Note:**  
Make sure PostgreSQL is running and the database specified in `config.py` exists before running migrations or seeding.