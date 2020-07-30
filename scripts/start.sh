echo "Starting server in Development mode"
gunicorn --bind 0.0.0.0:5000 wsgi:application -e ENV=development