from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now


class Module(models.Model):
    name = models.CharField(
        pgettext_lazy('Module field', 'name'),
        unique=True,
        max_length=128
    )
    description = models.TextField(
        pgettext_lazy('Module Field', 'description'),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        pgettext_lazy('Module field', 'created at'),
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        pgettext_lazy('Module field', 'updated at'),
        default=now
    )

    class Meta:
        app_label = 'module'

    def __str__(self):
        return self.name
