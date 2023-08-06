#!/usr/bin/env python3

# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Ginggar management script. For more information, search the web for "django manage.py".
"""

import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ginggar.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
