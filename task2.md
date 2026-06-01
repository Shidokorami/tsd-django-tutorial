# Task 2 — ORM relations queries

**Points:** 10

## Files

- `movies/models.py` — task **2.1**
- `movies/tasks/task2.py` — tasks **2.2**–**2.7**

## Commands

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
