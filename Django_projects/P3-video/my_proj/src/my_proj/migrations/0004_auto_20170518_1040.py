# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-18 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_proj', '0003_video_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='upload_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
