from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.


def home(req):
    return render(req, 'blog/home.html')


class homepage(ListView):
    model = models.Post
    template_name = 'blog/home.html'
