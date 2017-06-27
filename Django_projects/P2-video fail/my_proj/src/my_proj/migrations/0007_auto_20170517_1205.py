# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-17 10:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_proj', '0006_auto_20170517_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='added_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
