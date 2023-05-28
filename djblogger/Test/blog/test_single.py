import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestSinglePost:
    def test_singlePost_url(self, client, post_factory):
        post = post_factory()
        url = reverse('post-single', kwargs={'post': post.slug})
        res = client.get(url)
        assert res.status_code == 200
