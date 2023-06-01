import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse

pytestmark = pytest.mark.django_db


class Testsearch():

    def test_search_url(self, client):
        url = reverse('search')
        res = client.get(url)
        assert res.status_code == 200

    def test_search_htmx(self, client):
        header = {'HTTP_HX-Request': 'true'}
        url = reverse('search')
        res = client.get(url, **header)
        assertTemplateUsed(res, "blog/components/post_elements_search.html")

    def test_search_filter(self, client, post_factory):
        post = post_factory(title='testing-post')
        url = reverse('search')
        req = f'{url}?searchfield={post.title}'
        res = client.get(req)
        assert post.title in res.context['posts'][0].title
        assert post.title in res.content.decode('utf-8')
