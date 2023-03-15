#!/usr/bin/env python
import os
import sys
from distutils.dist import strtobool


def main():
    if strtobool(os.environ.get('debug')):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS.settings.dev')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMS.settings.pro')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError() from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
