# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-02 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpx_explorer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpx_file',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='gpx_file',
            name='key',
            field=models.CharField(default='xntRuIx9pySvsBh0iJHDLQYhB99POcku', max_length=32),
        ),
    ]
