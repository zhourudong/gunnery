#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # base_dir = os.getcwd()
    # base_dir1 = os.path.join(os.getcwd(), "gunnery")
    #
    # sys.path.append(base_dir1)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gunnery.settings.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
