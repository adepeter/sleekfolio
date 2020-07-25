from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    name = models.CharField(
        verbose_name=_('client name'),
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        blank=True,
        db_index=True
    )
    url = models.URLField(
        verbose_name=_('link to client page'),
        default=_('https://clienturl.com'),
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
