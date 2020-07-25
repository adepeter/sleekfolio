from django.shortcuts import render

from ..categories.models import Category
from ..projects.models import Project

TEMPLATE_URL = 'folioapps'


def homepage(request):
    template_name = f'{TEMPLATE_URL}/index.html'
    categories = Category.objects.all()
    projects = Project.objects.all()
    context = {'categories': categories, 'projects': projects}
    return render(request, template_name, context=context)
