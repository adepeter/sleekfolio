from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import Project, Screenshot


class ScreenshotStackedInline(admin.TabularInline):
    model = Screenshot
    extra = 5
    fields = ['preview_screenshot', 'image']
    readonly_fields = ['preview_screenshot']

    def preview_screenshot(self, obj):
        image_url = obj.image.url
        return mark_safe(f'<img src="{image_url}" height="120" width="120" alt="{obj.project.title} screenshot"/>')

    preview_screenshot.short_description = _('Preview screenshot')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['preview_image']
    list_display = [
        'preview_image',
        'title',
        'category',
        'slug',
        'stack',
        'description',
        'built_with',
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
            'fields': ['category']
        }),
        (_('Project preview image'), {
            'fields': ['preview', 'preview_image']
        }),
        (_('Project intro'), {
            'fields': [('title', 'slug')]
        }),
        (_('Project tech'), {
            'fields': [('stack', 'technologies'), 'built_with']
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

    def preview_image(self, obj):
        image_url = obj.preview.url
        return mark_safe(f'<img src="{image_url}" height="120" width="120" alt="{obj.title}"/>')

    preview_image.short_description = _('Preview')
