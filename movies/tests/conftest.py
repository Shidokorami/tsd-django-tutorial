import pytest

from movies.models import Model, ParentModel


@pytest.fixture(scope='session', autouse=True)
def ensure_postgres_for_tests():
    from config.postgres import ensure_postgres_running
    ensure_postgres_running()


@pytest.fixture(autouse=True)
def _use_fixtures_only(db):
    """
    Migrations seed demo rows (for dev / Task 3 on database `tutorial`).

    pytest-django uses a separate database (`test_tutorial`). The seed migration
    runs there too, so we clear tables before each test; fixtures then supply
    the only rows assertions rely on.
    """
    Model.objects.all().delete()
    ParentModel.objects.all().delete()
