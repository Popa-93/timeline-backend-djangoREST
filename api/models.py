from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db import models

from django.contrib.auth import get_user_model


class Timeline(models.Model):
    title = models.CharField(max_length=100, blank=True)

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='timelines')

    class Meta:
        verbose_name = "timeline"
        ordering = ['id']

    def __str__(self):
        return self.title


class Activity(models.Model):
    name = models.CharField(max_length=100)
    # avatar = models.ImageField(upload_to="photos/") # TODO
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='activities'
    )

    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"
        ordering = ['id']

    def __str__(self):
        return self.name


class Record(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    timeline = models.ForeignKey(
        Timeline, on_delete=models.CASCADE, related_name='records')

    class Meta:
        verbose_name = "record"
        ordering = ['id']

    def __str__(self):
        return self.title
