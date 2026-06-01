# Django ORM & DRF — Student Tutorial

## Introduction

This tutorial walks you through building a small **Movies REST API** using Django and Django REST Framework (DRF). You will work progressively through three tasks, each covering a key concept:

| Task | Topic | Points |
|------|-------|--------|
| [Task 1](docs/tasks.md#task-1--basic-orm-queries) | ORM basics — querying a single model | 5 |
| [Task 2](docs/tasks.md#task-2--orm-relations-queries) | ORM relations — ForeignKey and related queries | 10 |
| [Task 3](docs/tasks.md#task-3--django-rest-framework) | DRF — serializers, viewsets, and routing | 15 |

All task instructions and commands are in [docs/tasks.md](docs/tasks.md).  
A syntax reference is available in [docs/cheatsheet.md](docs/cheatsheet.md).

---

## Getting started

```bash
docker compose up -d --build
docker compose run --rm app python manage.py migrate
```

**GitHub Codespaces:** run `python manage.py` / `pytest` directly (no `docker compose run --rm app` prefix).

---

## Working on exercises

1. **Fork** this repository on GitHub.
2. Clone your fork and do your work there.
or
3. Create Codespaces
---
