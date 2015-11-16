# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('latest', models.BooleanField(default=True)),
                ('attendees', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='events.Attendance')),
                ('creator', models.ForeignKey(related_name='event_creator_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(to='events.Event'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
