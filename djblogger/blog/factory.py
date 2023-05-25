import factory
from factory.faker import faker
from django.contrib.auth.models import User
from .models import Post


fak = faker.Faker()


class factoryPost(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=20)
    subtitle = factory.Faker('sentence', nb_words=89)
    slug = factory.Faker('slug')
    author = User.objects.get_or_create(username='writer')[0]

    @factory.lazy_attribute
    def content(self):
        x = ''
        for _ in range(4):
            x += '\n' + fak.paragraph(nb_sentences=50) + '\n'
            return x

    status = 'published'


# creates a 100 posts in the database
# posts100 = factoryPost.create_batch(100)
