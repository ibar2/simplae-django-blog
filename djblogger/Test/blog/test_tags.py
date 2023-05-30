import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestListTags:
    def test_tag_urls(self, client, post_factory):
        post_factory(title='testing-tags', tags=['tag-testing'])
        url = reverse('tag-list', kwargs={'tag': 'tag-testing'})
        res = client.get(url)
        assert res.status_code == 200

    def test_htmx(self, client, post_factory):
        m = post_factory(title='testing-tag', tags=['tag-test'])
        header = {'HTTP_HX-Request': 'true'}
        url = reverse('tag-list', kwargs={'tag': m.tags.name})
        res = client.get(url, **header)
        assertTemplateUsed(res, "blog/components/tag_post_list.html")

