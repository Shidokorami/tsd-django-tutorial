import pytest

from movies.models import Director, Movie


@pytest.fixture(scope='session', autouse=True)
def ensure_postgres_for_tests():
    from config.postgres import ensure_postgres_running
    ensure_postgres_running()


@pytest.fixture(autouse=True)
def _use_fixtures_only(db):
    """
    Migrations seed demo rows (for dev / Task 3 on database `tutorial`).

    pytest-django uses `test_tutorial`. The seed migration runs there too;
    we clear tables before each test so fixtures supply the only rows under test.
    """
    Movie.objects.all().delete()
    Director.objects.all().delete()
