# Task 2 — ORM relations (ParentModel ↔ Model)

**Points:** 10 (running total: **15**)

Requires Task 1 tests to pass.

## Files

- `movies/models.py` — task **2.1** (`TODO: Task 2.1`)
- `movies/tasks/task2.py` — tasks **2.2**–**2.7** (`TODO: Task 2.x`)

## Commands

```bash
docker compose up -d --build
```

After **2.1** (add `ForeignKey` on `Model` → `ParentModel`, `related_name='models'`):

```bash
docker compose run --rm app python manage.py makemigrations
docker compose run --rm app python manage.py migrate
```

Tests:

```bash
docker compose run --rm app pytest movies/tests/test_task1.py movies/tests/test_task2.py -v
```

Or only Task 2:

```bash
docker compose run --rm app pytest movies/tests/test_task2.py -v
```

**GitHub Codespaces:** omit `docker compose run --rm app` (run `python manage.py` / `pytest` directly).
