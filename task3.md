# Task 3 — REST API (Django REST Framework)

**Points:** 15 (running total: **30**)

Requires Task 1 and Task 2 tests to pass.

## Files

- `movies/serializers.py` — tasks **3.1**, **3.2** (`ModelApiSerializer`)
- `movies/views.py` — tasks **3.3**, **3.5** (`ModelApiViewSet`)
- `movies/urls.py` — task **3.4** (router already registered)

## Commands

```bash
docker compose up -d --build
docker compose run --rm app python manage.py migrate
docker compose run --rm app python manage.py runserver 0.0.0.0:8000
```

Open in a browser (required check):

- [http://127.0.0.1:8000/api/models/](http://127.0.0.1:8000/api/models/)

In GitHub Codespaces, use the forwarded URL for port **8000** with path `/api/models/`.

**GitHub Codespaces:** omit `docker compose run --rm app` for `migrate` / `runserver`.

Optional:

```bash
curl -s http://127.0.0.1:8000/api/models/
```
