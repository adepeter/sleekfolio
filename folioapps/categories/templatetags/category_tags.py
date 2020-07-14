from django import template
from django.db.models import Count

from ..models import Category

register = template.Library()

@register.simple_tag
def get_all_categories(project_queryset):
    queryset = Category.objects.annotate(
        count_projects=Count('projects')
    ).filter(projects__in=project_queryset)
    return queryset
