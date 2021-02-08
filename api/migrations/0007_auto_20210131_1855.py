# Generated by Django 3.1.4 on 2021-01-31 17:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210128_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='activityID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.activity'),
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='record',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
