import pytest

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_return(self, post_factory):
        post = post_factory(title='test')
        assert post.__str__() == 'test'

    def test_tags(self, post_factory):
        x = post_factory(title="test", tags=['t-tag'])
        assert x.tags.count() == 1
