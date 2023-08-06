# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Helpers for user scripting.
"""

import json
import typing as t

import django.conf
import django.contrib.auth.models

import ginggar.main.models


def is_execute_user_script_enabled(user: "django.contrib.auth.models") -> bool:
    """
    Returns whether backend side user scripting is available for a given user.
    """
    if django.conf.settings.SINGLE_USER_MODE:
        return True
    else:
        return user.username in ginggar.main.models.UserConfiguration.get(None, "allowuserscriptingfor", [])


def execute_user_script(user: "django.contrib.auth.models", scriptname: str, *args: t.Any) -> None:
    """
    Executes a user script.

    This is not always enabled and is a noop otherwise. See the documentation for more details.
    """
    if not is_execute_user_script_enabled(user):
        return
    import ginggar.main.models
    code = ginggar.main.models.UserConfiguration.get(user, scriptname)
    if code:
        globl = {}
        locl = {}
        exec(code, globl, locl)
        locl[scriptname](*args)
