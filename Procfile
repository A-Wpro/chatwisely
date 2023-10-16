# Write the Procfile
#web: gunicorn app:server
worker: python app.py
web: gunicorn -b 0.0.0.0:$PORT app:server
