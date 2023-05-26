from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):

    options = [
        ('draft', 'Draft'),
        ('published', "published")
    ]

    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=18)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    content = models.TextField()
    status = models.CharField(choices=options, max_length=10, default='draft')
    createdat = models.DateField(auto_now_add=True, editable=False)
    updataedat = models.DateField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = '-createdat',

    def __str__(self) -> str:
        return self.title
