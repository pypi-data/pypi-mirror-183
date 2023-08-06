from wagtail.api import APIField
from django.db import models
from wagtail.images import get_image_model_string
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.api.fields import ImageRenditionField
from django.conf import settings


class PageBannerMixin(models.Model):
    banner_title = models.TextField(max_length=100, blank=False, default="")
    banner_subtitle = models.TextField(max_length=500, blank=False, default="")
    banner_image = models.ForeignKey(get_image_model_string(), on_delete=models.PROTECT, blank=False, null=True,
                                     default=None)

    page_banner_panels = [
        MultiFieldPanel(
            heading="Page Banner",
            children=[
                FieldPanel('banner_title'),
                FieldPanel('banner_subtitle'),
                FieldPanel('banner_image'),
            ]
        ),
    ]

    class Meta:
        abstract = True
