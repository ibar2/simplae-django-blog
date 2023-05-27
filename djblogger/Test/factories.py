import factory
from django.contrib.auth.models import User
from djblogger.blog.models import Post


class userfactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = 'test'
    username = 'test'
    is_superuser = True
    is_staff = True


class postFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = 'x'
    subtitle = 'x'
    slug = 'x'
    author = factory.SubFactory(userfactory)
    content = 'xxx'
    status = 'published'

    @factory.post_generation
    def tags(self, created, extracted, **kwargs):
        if not created:
            return

        if extracted:
            self.tags.add(*extracted)
