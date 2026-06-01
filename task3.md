# Task 3 — Django REST Framework

**Points:** 15


## Files

- `movies/serializers.py` — tasks **3.1**, **3.2**
- `movies/views.py` — tasks **3.3**,
- `movies/urls.py` — task **3.4**

## Commands

```bash
docker compose up -d --build
docker compose run --rm app python manage.py migrate
docker compose run --rm app python manage.py runserver 0.0.0.0:8000
```

Open in a browser (required check):

- [http://127.0.0.1:8000/api/movies/](http://127.0.0.1:8000/api/movies/)

In GitHub Codespaces, use the forwarded URL for port **8000** with path `/api/movies/`.

Optional:

```bash
curl -s http://127.0.0.1:8000/api/movies/
```
