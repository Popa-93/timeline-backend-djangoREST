from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=100)

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


#####################################################


@ receiver(pre_delete, sender=Record, dispatch_uid='record_delete_signal')
def prevent_cascade_deletion_on_manytomany(sender, instance, using, **kwargs):
    instance.activities.remove()
