import os

from django.utils.timezone import now as timezone_now


def image_upload_hander(instance, filename):
    now = timezone_now()
    slug = instance.category.slug
    base, ext = os.path.splitext(filename)
    return f"projects/{slug}/{now:%Y%m%d%H%M%S}{ext.lower()}"
