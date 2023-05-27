from django.shortcuts import render, get_object_or_404
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


def post_single(req, post):
    post = get_object_or_404(models.Post, slug=post, status='published')
    return render(req, 'blog/single_post.html', {
        'post_content': post
    })
