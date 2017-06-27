from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.db import models
from django.contrib.auth.models import User

from my_proj.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
