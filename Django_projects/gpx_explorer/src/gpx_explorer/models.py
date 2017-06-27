from django.db import models
from django import forms
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.utils.crypto import get_random_string

import os

def path_and_rename(instance, filename):
    upload_to = 'uploads/'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.key, ext)
    return os.path.join(upload_to, filename)

class GPX_file(models.Model):
    key = models.CharField(max_length=32, default=get_random_string(length=32))
    file = models.FileField(upload_to=path_and_rename)
    name = models.CharField(max_length=100, default="")
    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    #restricted_to = models.ForeignKey(Group)