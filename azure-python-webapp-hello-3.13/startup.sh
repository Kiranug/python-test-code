#!/usr/bin/env bash
set -euo pipefail
# Bind to the port provided by Azure (PORT) or fallback to 8000
exec gunicorn --workers 2 --timeout 120 --bind 0.0.0.0:${PORT:-8000} app:app