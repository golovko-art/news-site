from django import template

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_of_categories')
def get_categories():
    return Category.objects.all()
