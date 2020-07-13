from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from .models import Project

TEMPLATE_URL = 'folioapps/projects'


class ProjectDetail(DetailView):
    model = Project
    template_name = f'{TEMPLATE_URL}/project_detail.html'
    query_pk_and_slug = True
    context_object_name = 'project'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category__slug=self.kwargs['category_slug'])


class ProjectSearch(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = f'{TEMPLATE_URL}/project_search.html'

    def get(self, request, *args, **kwargs):
        self.search_keyword = request.GET.get('q', None)
        if self.search_keyword is None:
            return redirect('sleekfolio:homepage')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()
