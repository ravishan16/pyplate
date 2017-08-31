#!/bin/sh
set -e

echo "Running Production Application"
exec gunicorn -w 4 -b 0.0.0.0:4000 --access-logfile - flaskapp:create_app\(config_name=\"$FLASKAPP_ENV\"\)

