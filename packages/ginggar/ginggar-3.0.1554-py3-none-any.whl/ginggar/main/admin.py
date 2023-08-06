# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Preparations for Django admin panel.
"""

from django.contrib import admin

from ginggar.main.models import *


admin.site.register(Feed)
admin.site.register(NewsMessage)
admin.site.register(Tag)
admin.site.register(UserConfiguration)
admin.site.register(TagPropagationRule)
