from django.db import models
from django.utils.translation import gettext_lazy as _


class Screenshot(models.Model):
    project = models.ForeignKey(
        'projects.Project',
        verbose_name=_('project'),
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to='images'
    )

    def __str__(self):
        return self.project
