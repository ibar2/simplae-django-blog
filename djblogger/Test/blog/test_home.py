import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


class TestHomePage:
    def test_home_url(self, client):
        url = reverse('home')
        res = client.get(url)
        assert res.status_code == 200

    def test_htmx(self, client):
        header = {'HTTP_HX-Request': 'true'}
        res = client.get("/", **header)
        assertTemplateUsed(res, "blog/components/post_list.html")
