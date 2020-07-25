import os

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

def upload_screenshots_to(instance, filename):
    now = timezone.now()
    project_slug = instance.project.slug
    project_category_slug = instance.project.category.slug
    base, ext = os.path.splitext(filename)
    return f"projects/{project_category_slug}/{project_slug}/screenshots/{now:%Y%m%d%H%M%S}{ext.lower()}"

class Screenshot(models.Model):
    project = models.ForeignKey(
        'projects.Project',
        verbose_name=_('project'),
        on_delete=models.CASCADE,
        related_name='screenshots'
    )
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to=upload_screenshots_to,
    )

    def __str__(self):
        return self.project.title
