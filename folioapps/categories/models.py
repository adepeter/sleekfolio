from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
        unique=True
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        blank=True
    )
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Categories')
        ordering = ['name']