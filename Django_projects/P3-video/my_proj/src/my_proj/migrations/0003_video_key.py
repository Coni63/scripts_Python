# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-18 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_proj', '0002_remove_video_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='key',
            field=models.CharField(default='', max_length=11),
        ),
    ]
