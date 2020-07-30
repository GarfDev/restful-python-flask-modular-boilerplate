echo "Starting server in Development mode"
gunicorn --bind 0.0.0.0:5000 wsgi:application --capture-output --enable-stdio-inheritance -e ENV=development 