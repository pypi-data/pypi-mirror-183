# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import os
import sys

me = os.path.dirname(os.path.abspath(__file__))
sys.path.append(me)
os.chdir(me)
os.environ["DJANGO_SETTINGS_MODULE"] = "ginggar.settings"
import django.core.wsgi
application = django.core.wsgi.get_wsgi_application()
