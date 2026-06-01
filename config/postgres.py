from pathlib import Path
import os
import shutil
import subprocess
import time

PROJECT_ROOT = Path(__file__).resolve().parent.parent

_SETUP_HINT = (
    'PostgreSQL is not running on localhost:5432.\n\n'
    'Start the database with Docker (Docker Desktop with WSL integration enabled):\n'
    '  docker compose up -d db\n'
)


def _load_env() -> None:
    env_file = PROJECT_ROOT / '.env'
    if env_file.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(env_file)
        except ImportError:
            pass


def _connection_params() -> dict[str, str]:
    _load_env()
    return {
        'host': os.environ.get('POSTGRES_HOST', 'localhost'),
        'port': os.environ.get('POSTGRES_PORT', '5432'),
        'dbname': os.environ.get('POSTGRES_DB', 'tutorial'),
        'user': os.environ.get('POSTGRES_USER', 'tutorial'),
        'password': os.environ.get('POSTGRES_PASSWORD', 'tutorial'),
    }


def _is_local_host(host: str) -> bool:
    return host in ('localhost', '127.0.0.1')


def _postgres_ready() -> bool:
    try:
        import psycopg
        psycopg.connect(**_connection_params()).close()
        return True
    except Exception:
        return False


def _docker_available() -> bool:
    if not shutil.which('docker'):
        return False
    try:
        subprocess.run(
            ['docker', 'info'],
            check=True,
            capture_output=True,
        )
        return True
    except (subprocess.CalledProcessError, OSError):
        return False


def _start_postgres_container() -> None:
    try:
        subprocess.run(
            ['docker', 'compose', 'up', '-d', 'db'],
            check=True,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr or ''
        raise RuntimeError(_SETUP_HINT) from exc


def ensure_postgres_running() -> None:
    params = _connection_params()
    if not _is_local_host(params['host']):
        return
    if _postgres_ready():
        return
    if not _docker_available():
        raise RuntimeError(_SETUP_HINT)
    _start_postgres_container()
    for _ in range(30):
        if _postgres_ready():
            return
        time.sleep(1)
    raise RuntimeError(_SETUP_HINT)
