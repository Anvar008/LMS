#!/bin/sh
# Entrypoint для Django-контейнера LMS_Copy.
# Запускается как пользователь app (см. Dockerfile), поэтому sudo/chown не нужны.
set -eu

DB_HOST="${DB_HOST:-db}"
DB_PORT="${DB_PORT:-5432}"
DB_WAIT_TIMEOUT="${DB_WAIT_TIMEOUT:-60}"

RUN_MIGRATIONS="${RUN_MIGRATIONS:-True}"
RUN_COLLECTSTATIC="${RUN_COLLECTSTATIC:-True}"

log() {
    echo "[entrypoint] $*"
}

wait_for_db() {
    log "Waiting for database at ${DB_HOST}:${DB_PORT} (timeout ${DB_WAIT_TIMEOUT}s)..."
    python - <<'PY'
import os
import socket
import sys
import time

host = os.environ.get("DB_HOST", "db")
port = int(os.environ.get("DB_PORT", "5432"))
timeout = int(os.environ.get("DB_WAIT_TIMEOUT", "60"))

deadline = time.monotonic() + timeout
while True:
    try:
        with socket.create_connection((host, port), timeout=2):
            break
    except OSError:
        if time.monotonic() >= deadline:
            print(f"[entrypoint] Database {host}:{port} is not reachable", file=sys.stderr)
            sys.exit(1)
        time.sleep(1)
PY
    log "Database is up."
}

is_true() {
    case "$1" in
        [Tt]rue|TRUE|1|[Yy]es|YES) return 0 ;;
        *) return 1 ;;
    esac
}

# Подготовку (БД, миграции, статика) делаем только для запуска сервера.
# Для `docker run image bash` или `docker compose run web python manage.py ...`
# контейнер стартует сразу, без ожидания БД.
case "${1:-}" in
    gunicorn|daphne|uvicorn)
        wait_for_db

        if is_true "$RUN_MIGRATIONS"; then
            log "Applying migrations..."
            python manage.py migrate --noinput
        fi

        if is_true "$RUN_COLLECTSTATIC"; then
            log "Collecting static files..."
            python manage.py collectstatic --noinput
        fi
        ;;
esac

log "Starting: $*"
exec "$@"