from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('search/', views.ProjectSearch.as_view(), name='project_search'),
    path('<slug:category_slug>/<int:id>/<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail'),
]