# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-17 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_proj', '0002_remove_video_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
