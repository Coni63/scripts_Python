# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-20 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_proj', '0006_remove_video_restricted_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='restricted_to',
            field=models.CharField(default='', max_length=11),
        ),
    ]
