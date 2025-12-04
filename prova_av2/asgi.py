import os

from django.core.asgi import get_asgi_application

# servidor async padrão, nada demais
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prova_av2.settings')

application = get_asgi_application()
