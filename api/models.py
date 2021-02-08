from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db import models

from django.contrib.auth import get_user_model
import datetime


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
    name = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True)
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
    # Add user filed to protect data
    # => filter on timeline ensure functionality, ot security
    # => allow filering per user on API call otherwise a smart guy could request someone else records
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='records'
    )

    title = models.CharField(max_length=100, blank=True)
    date = models.DateField(default=datetime.date.today)
    description = models.TextField(blank=True)
    activityID = models.ForeignKey(
        Activity, blank=True, null=True, on_delete=models.PROTECT)
    timelineID = models.ForeignKey(
        Timeline, on_delete=models.CASCADE, related_name='records')

    class Meta:
        verbose_name = "record"
        ordering = ['id']

    def __str__(self):
        return self.title
