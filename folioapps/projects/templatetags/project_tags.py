from django import template
from django.db.models import Q

from ..models import Project

TEMPLATE_URL = 'folioapps/projects/_partials/'

register = template.Library()


@register.inclusion_tag(f'{TEMPLATE_URL}/_related_projects.html')
def related_projects(project, items=13):
    technologies_arr = project.technologies
    projects = Project.objects.filter(
        ~Q(id=project.id) &
        Q(technologies__contained_by=technologies_arr)).order_by('?')
    return {'projects': projects}
