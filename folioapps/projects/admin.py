from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Project, Screenshot


class ScreenshotStackedInline(admin.StackedInline):
    model = Screenshot
    extra = 5


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = [
        'preview',
        'title',
        'category',
        'slug',
        'description',
        'technologies',
        'is_completed',
        'date_started',
        'date_completed',
        'demo_url',
        'repo_url',
    ]
    list_filter = [
        'category',
        'stack',
        'is_completed',
    ]
    search_fields = [
        'title',
        'description',
        'slug'
    ]
    prepopulated_fields = {
        'slug': ('title',)
    }
    fieldsets = [
        (_('Project categorisation'), {
            'fields': [('category', 'stack')]
        }),
        (_('Project preview image'), {
            'fields': ['preview']
        }),
        (_('Project intro'), {
            'fields': [('title', 'slug'), 'technologies']
        }),
        (_('Project detail'), {
            'fields': ['description']
        }),
        (_('Project status'), {
            'fields': ['is_completed']
        }),
        (_('Project important dates'), {
            'fields': ['date_started', 'date_completed']
        }),
        (_('Important links'), {
            'fields': ['demo_url', 'repo_url']
        }),
    ]
    date_hierarchy = 'date_completed'
    inlines = [ScreenshotStackedInline]
