from taggit.models import Tag

from django import template
register = template.Library()


@register.inclusion_tag('blog/components/tag_cloud.html')
def side_tag_cloud():
    x = Tag.objects.all()
    return {'tags': x}
