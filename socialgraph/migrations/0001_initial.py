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
            name='UserLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('from_user', models.ForeignKey(related_name='following_set', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='follower_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userlink',
            unique_together=set([('to_user', 'from_user')]),
        ),
    ]
