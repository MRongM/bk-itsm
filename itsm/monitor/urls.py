# -*- coding: utf-8 -*-
from django.conf.urls import url

from itsm.monitor.views import healthz, ping, login_ping

urlpatterns = [
    # main
    url(r"^healthz/$", healthz),
    url(r"^ping/", ping),
    url(r"^login_ping/", login_ping),
]
