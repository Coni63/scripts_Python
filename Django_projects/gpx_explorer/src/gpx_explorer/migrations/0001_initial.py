# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-02 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gpx_explorer.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GPX_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='MHeAI9r9Ti6hv5dxSAB29MPSBARmgJkc', max_length=32)),
                ('file', models.FileField(upload_to=gpx_explorer.models.path_and_rename)),
                ('name', models.CharField(default='', max_length=100)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
