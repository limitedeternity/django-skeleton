# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        if request.method == 'GET':
            return render(request, "index.html", context=None)
