#!/usr/bin/env python
# script que roda os comandos do django, nada chique
import os
import sys


def main():
    # só chama o Django pra rodar o que pedirem
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prova_av2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
