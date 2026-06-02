# Tasks

## Task 1 — Basic ORM queries

**Points:** 5

### Files

- `movies/tasks/task1.py` — tasks **1.1**–**1.6**

### Commands

```bash
docker compose up -d --build
docker compose run --rm app python manage.py migrate
docker compose run --rm app pytest movies/tests/test_task1.py -v
```

**GitHub Codespaces:** Use the same commands without the `docker compose run --rm app` prefix (e.g. `python manage.py migrate`).

---

## Task 2 — ORM relations queries

**Points:** 10

### Files

- `movies/models.py` — task **2.1**
- `movies/tasks/task2.py` — tasks **2.2**–**2.4**

### Commands

After **2.1** (add the relation on `Movie`):

```bash
docker compose run --rm app python manage.py makemigrations
docker compose run --rm app python manage.py migrate
```

Tests:

```bash
docker compose run --rm app pytest movies/tests/test_task2.py -v
```

**GitHub Codespaces:** omit `docker compose run --rm app` (run `python manage.py` / `pytest` directly).

---

## Task 3 — Django REST Framework

**Points:** 15

### Files

- `movies/serializers.py` — tasks **3.1**, **3.2**
- `movies/views.py` — tasks **3.3**, **3.4** (`MovieViewSet`: `list`, `retrieve`)
- `movies/urls.py` — task **3.5** (`router.register`)

### Commands

```bash
docker compose up -d --build
docker compose run --rm app python manage.py migrate
docker compose run --rm --service-ports app python manage.py runserver 0.0.0.0:8000
```

Open in a browser (required check):

- [http://127.0.0.1:8000/api/movies/](http://127.0.0.1:8000/api/movies/)

In GitHub Codespaces, use the forwarded URL for port **8000** with path `/api/movies/`.

Optional:

```bash
curl -s http://127.0.0.1:8000/api/movies/
```
