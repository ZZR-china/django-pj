from django import template
from django.db.models.aggregates import Count
from ..models import Category

register = template.Library()


@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_article=Count('article')).filter(num_article__gt=0)
