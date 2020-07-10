from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ...cores.utils.choice import Choicify

from .. import constants

choicify_stacks = Choicify(constants.STACK_CHOICES)


class Project(models.Model):
    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('category'),
        on_delete=models.CASCADE,
        help_text=_('Type of category project belongs to')
    )
    preview = models.ImageField(
        verbose_name=_('preview'),
        upload_to='images',
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
    is_completed = models.BooleanField(
        verbose_name=_('project completion status'),
        default=False,
        help_text=_('Completion state of project')
    )
    demo_url = models.URLField(
        verbose_name=_('demo link'),
        default='https://',
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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'slug'],
                name='unique_title_and_slug'
            )
        ]
        ordering = ['title']
