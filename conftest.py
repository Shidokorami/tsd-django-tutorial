import pytest

from config.postgres import ensure_postgres_running


@pytest.fixture(scope='session', autouse=True)
def _ensure_postgres():
    ensure_postgres_running()
