# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-08 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0004_auto_20170307_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote_event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.CharField(default='0', max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='score',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterUniqueTogether(
            name='vote_event',
            unique_together=set([('user', 'event', 'vote_type')]),
        ),
    ]
