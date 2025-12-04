import os

from django.core.wsgi import get_wsgi_application

# versão sync do servidor, o básico do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prova_av2.settings')

application = get_wsgi_application()
