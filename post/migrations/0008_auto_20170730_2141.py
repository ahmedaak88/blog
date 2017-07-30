# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-30 21:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0007_auto_20170730_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='event_slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
