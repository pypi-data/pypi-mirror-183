# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Django url mappings for Ginggar.
"""

from django.urls import path
from django.contrib import admin

import ginggar.main.views


urlpatterns = [

    path("", ginggar.main.views.IndexPageView.as_view()),
    path("login/", ginggar.main.views.LoginPageView.as_view()),
    path("admin/", admin.site.urls),

    path("api/accounts/actions/login/", ginggar.main.views.AccountsActionLoginView.as_view()),
    path("api/accounts/actions/logout/", ginggar.main.views.AccountsActionLogoutView.as_view()),

    path("api/messages/", ginggar.main.views.MessagesView.as_view()),
    path("api/messages/<int:msgid>/", ginggar.main.views.MessageView.as_view()),

    path("api/tags/", ginggar.main.views.TagsView.as_view()),
    path("api/tags/<str:tag>/", ginggar.main.views.TagView.as_view()),

    path("api/tagpropagationrules/", ginggar.main.views.TagPropagationRulesView.as_view()),
    path("api/tagpropagationrules/<int:ruleid>/", ginggar.main.views.TagPropagationRuleView.as_view()),

    path("api/filters/", ginggar.main.views.FiltersView.as_view()),
    path("api/filters/<str:filtername>/", ginggar.main.views.FilterView.as_view()),

    path("api/feeds/", ginggar.main.views.FeedsView.as_view()),
    path("api/feeds/<int:feedid>/", ginggar.main.views.FeedView.as_view()),
    path("api/feeds/actions/crawl/", ginggar.main.views.FeedsActionCrawlView.as_view()),

    path("api/configs/", ginggar.main.views.UserConfigurationsView.as_view()),
    path("api/configs/<str:key>/", ginggar.main.views.UserConfigurationView.as_view()),

]
