# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Some helping hands for ginggar.main.views.
"""

import json
import typing as t
import urllib.parse

import django.conf
import django.contrib.auth.decorators
import django.contrib.auth.models
import django.core.serializers
import django.db.models
import django.http
import django.middleware.csrf
import django.shortcuts
import django.utils.decorators

import ginggar.main.models
import ginggar.main.userscripting


def login_required(fct: t.Callable) -> t.Callable:
    """
    Decorator for requiring an authenticated user for a view method.

    A user who visits such a view without being logged in will be forwarded to the login page and redirected back
    afterwards.
    """
    if django.conf.settings.SINGLE_USER_MODE:
        def _singleuser(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                django.contrib.auth.login(request, _get_default_admin_user())
            return fct(self, request, *args, **kwargs)
        return _singleuser
    else:
        return django.utils.decorators.method_decorator(django.contrib.auth.decorators.login_required)(fct)


def render_template(templatefile: str, *, request: django.http.HttpRequest,
                    templateargs: t.Optional[t.Dict] = None, ginggarcontextargs: t.Optional[t.Dict] = None) -> str:
    """
    Renders a template with some common data available in its context.
    """
    return django.shortcuts.render(
        request, templatefile, {
            "ginggarcontext": json.dumps({
                "backenduserscriptingavailable":
                    bool(ginggar.main.userscripting.is_execute_user_script_enabled(request.user)),
                "csrftoken": django.middleware.csrf.get_token(request),
                "issuperuser": request.user.is_superuser,
                "subsite": django.conf.settings.SUB_SITE,
                "singleusermode": bool(django.conf.settings.SINGLE_USER_MODE),
                **(ginggarcontextargs or {})
            }),
            "subsite": django.conf.settings.SUB_SITE,
            **(templateargs or {})})


def _get_default_admin_user() -> django.contrib.auth.models.User:
    """
    Finds or creates the default admin user.
    """
    adminuser = django.contrib.auth.authenticate(username="admin", password="admin")
    if not adminuser:
        adminuser = django.contrib.auth.models.User.objects.create_user("admin", "admin@localhost", "admin")
        adminuser.is_superuser = True
        adminuser.is_staff = True
        adminuser.save()
    return adminuser


def ensure_ginggar_initialized() -> bool:
    """
    Ensures that Ginggar is initialized (e.g. a factory default admin user was created).

    Does the initialization on first run. Returns `True` in this case.
    """
    if not ginggar.main.models.UserConfiguration.get(None, "isinitialized", False):
        ginggar.main.models.UserConfiguration.set(None, "isinitialized", True)
        if not django.conf.settings.EXTERNAL_AUTH_HELPER:
            _get_default_admin_user()
        return True


def request_body_object(request: django.http.HttpRequest) -> t.Optional[t.Any]:
    """
    Deserializes the request body. Typically this is a dictionary of arguments.
    """
    if request.content_type == "application/x-www-form-urlencoded":
        return {k: v[0] for k, v in urllib.parse.parse_qs(request.body.decode()).items()}
    else:
        return json.loads(request.body)


def modellist_to_dictlist(models: t.List[django.db.models.Model]) -> t.List[t.Dict]:
    """
    Returns a list of serializable dicts for a list of native models.
    """
    return json.loads(django.core.serializers.serialize("json", models))
