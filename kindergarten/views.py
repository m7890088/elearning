from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'kindergarten/index.html'


class ClassView(TemplateView):
    template_name = 'kindergarten/class.html'

class LoginView(TemplateView):
    template_name = 'kindergarten/login.html'
