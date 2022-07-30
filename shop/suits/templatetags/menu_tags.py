from django import template
from suits.models import Category


register = template.Library()


def get_all_categories():
    return Category.objects.all()

#@register.simple_tag()
#def get_categories():
#    """Вывод всех категорий"""
#    return Category.objects.all()


@register.inclusion_tag('suits/include/tags/top_menu.html')
def get_categories():
    category = get_all_categories()
    return {"list_category": category}
#filter(parent__isnull=True)

@register.inclusion_tag('suits/include/tags/middle_menu.html')
def get_menu_categories():
    category = Category.objects.filter(level=1).order_by('name')
    return {"list_category": category}