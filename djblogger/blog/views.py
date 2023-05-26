# from django.shortcuts import render
from typing import List
from django.views.generic import ListView
from . import models
# Create your views here.


class homepage(ListView):
    model = models.Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post_list.html"
        return "blog/home.html"
