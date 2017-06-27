from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings


class Video(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=100, default="test")
    views_counter = models.PositiveIntegerField(default='0')
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL)