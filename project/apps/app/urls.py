# -*- coding: utf-8 -*-
from django.conf.urls import url

from project.apps.app import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
]
