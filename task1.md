# Task 1 — basic ORM queries

**Points:** 5

## Files

- `movies/tasks/task1.py` — tasks **1.1**–**1.6**

## Commands

```bash
docker compose up -d --build
docker compose run --rm app python manage.py migrate
docker compose run --rm app pytest movies/tests/test_task1.py -v
```

**GitHub Codespaces:** Use the same commands without the `docker compose run --rm app` prefix (e.g. `python manage.py migrate`).
