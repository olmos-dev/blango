import os
from configurations.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blango.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")  # Igual que en manage.py

application = get_wsgi_application()
