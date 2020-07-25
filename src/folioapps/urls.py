from django.urls import include, path

app_name = 'sleekfolio'

urlpatterns = [
    path('', include('folioapps.pages.urls')),
    path('projects/', include('folioapps.projects.urls', namespace='projects')),
]