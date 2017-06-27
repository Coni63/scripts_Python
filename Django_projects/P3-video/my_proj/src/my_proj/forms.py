from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.db import models
from django.contrib.auth.models import User, Group

from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        widgets = {
            'url': forms.TextInput(attrs={
                'placeholder': 'https://www.youtube.com/watch?v=',
                'required': True,
                'style':'width:250px;'
            })
        }
        fields = ['url', 'restricted_to']
        restricted_to = forms.ModelChoiceField(queryset=None)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        self.usergroups = Group.objects.filter(user=self.user)
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['restricted_to'].queryset = self.usergroups