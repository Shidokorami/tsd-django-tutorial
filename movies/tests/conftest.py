import pytest


@pytest.fixture(scope='session', autouse=True)
def ensure_postgres_for_tests():
    from config.postgres import ensure_postgres_running
    ensure_postgres_running()
