#!/usr/bin/env python PYTHONDONTWRITEBYTECODE=1 python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mvp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
