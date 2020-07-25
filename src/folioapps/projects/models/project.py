import os

from django.contrib.postgres.fields import ArrayField, HStoreField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ...cores.utils.choice import Choicify

from .. import constants

choicify_stacks = Choicify(constants.STACK_CHOICES)

def upload_preview_to(instance, filename):
    now = timezone.now()
    category_slug = instance.category.slug
    project_slug = instance.slug
    base, ext = os.path.splitext(filename)
    return f"projects/{category_slug}/{project_slug}/{now:%Y%m%d%H%M%S}{ext.lower()}"


class Project(models.Model):
    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('category'),
        on_delete=models.CASCADE,
        related_name='projects',
        help_text=_('Type of category project belongs to')
    )
    preview = models.ImageField(
        verbose_name=_('preview'),
        upload_to=upload_preview_to,
        blank=True,
        null=True,
        help_text=_('Preview image for project')
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        blank=True,
        db_index=True
    )
    stack = models.CharField(
        verbose_name=_('stack'),
        max_length=len(choicify_stacks),
        choices=choicify_stacks.get_choices,
        blank=True,
        help_text=_('Stack type for project')
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
        help_text=_('Succinct description of project')
    )
    technologies = ArrayField(
        models.SlugField(),
        verbose_name=_('technologies'),
        blank=True,
        null=True,
        help_text=_('Technologies with which project was built')
    )
    built_with = HStoreField(
        verbose_name=_('built with'),
        blank=True,
        null=True,
        help_text=_('Tools or languages that were employed to build the project')
    )
    is_completed = models.BooleanField(
        verbose_name=_('project completion status'),
        default=False,
        help_text=_('Completion state of project')
    )
    demo_url = models.URLField(
        verbose_name=_('demo link'),
        default='https://demo-link.com/',
        blank=True,
        help_text=_('Link to preview project')
    )
    repo_url = models.URLField(
        verbose_name=_('repo link'),
        default='https://github.com/',
        help_text=_('Repository url for project')
    )
    date_started = models.DateField(
        verbose_name=_('project start date'),
        default=timezone.now,
        help_text=_('Date project was commenced')
    )
    date_completed = models.DateField(
        verbose_name=_('date of completion'),
        default=timezone.now,
        help_text=_('Date project was completed')
    )

    def get_absolute_url(self):
        kwargs = {
            'category_slug': self.category.slug,
            'id': self.id,
            'slug': self.slug
        }
        return reverse('sleekfolio:projects:project_detail', kwargs=kwargs)

    def __str__(self):
        return f'{self.title} - {self.category}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'slug'],
                name='unique_title_and_slug'
            )
        ]
        ordering = ['title']
