#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#This is yashash just checking to commit my changes over git.
#just checking don't get mad at me hahahhaha
# Aaj kuch padha? End sem ke liye?
#pagal launde
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurant.settings')
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
