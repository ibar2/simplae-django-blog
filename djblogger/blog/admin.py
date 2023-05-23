from django.contrib import admin
from .models import Post
from django.contrib.auth.models import Group


class PostMeta(admin.ModelAdmin):
    list_display = ['title', 'author', 'status']


admin.site.register(Post, PostMeta)
admin.site.unregister(Group)
