from django import template

register = template.Library()


@register.simple_tag(name='project_shots_by_count')
def project_screenshots_by_count(project, count=2):
    try:
        return project.screenshots.all()[:count]
    except KeyError:
        return project.screenshots.all[:1]
