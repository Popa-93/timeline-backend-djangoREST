from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db import models

from django.contrib.auth import get_user_model


class Activity(models.Model):
    name = models.CharField(max_length=100)

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='activities',
        default=None
    )

    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"
        ordering = ['id']

    def __str__(self):
        return self.name


class Record(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    activities = models.ManyToManyField(Activity)

    class Meta:
        verbose_name = "record"
        ordering = ['id']

    def __str__(self):
        return self.title


# Prevent cascade deletion on record or activity deletion
@ receiver(pre_delete, sender=Record, dispatch_uid='record_delete_signal')
def prevent_cascade_deletion_on_manytomany(sender, instance, using, **kwargs):
    instance.activities.remove()
