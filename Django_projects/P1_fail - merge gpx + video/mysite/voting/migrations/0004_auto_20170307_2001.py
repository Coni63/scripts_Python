# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-07 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20170307_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_type',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
