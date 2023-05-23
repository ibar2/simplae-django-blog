from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.


class homepage(ListView):
    model = models.Post
    template_name = 'blog/home.html'
