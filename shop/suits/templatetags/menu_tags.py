from django import template
from suits.models import Category


register = template.Library()


#@register.simple_tag()
#def get_categories():
#    """Вывод всех категорий"""
#    return Category.objects.all()


@register.inclusion_tag('suits/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.all().order_by("name")
    return {"list_category": category}
#filter(parent__isnull=True)