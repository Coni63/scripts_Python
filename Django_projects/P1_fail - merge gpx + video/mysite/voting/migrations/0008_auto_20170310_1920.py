# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-10 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_auto_20170310_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
