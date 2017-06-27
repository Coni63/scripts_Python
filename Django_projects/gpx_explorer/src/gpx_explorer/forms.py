from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.db import models
from django.contrib.auth.models import User, Group

from .models import GPX_file


class GPX_fileForm(forms.ModelForm):
    class Meta:
        model = GPX_file
        widgets = {
            'file' : forms.FileInput(attrs={'class': 'form-control', 'accept': '.gpx', 'id':'upload_file'}),
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Nom du parcours', 'id':'name'}),
        }
        fields = ['file', 'name']
        # restricted_to = forms.ModelChoiceField(queryset=None)

    # def __init__(self, user, *args, **kwargs):
    #     self.user = user
    #     self.usergroups = Group.objects.filter(user=self.user)
    #     super(VideoForm, self).__init__(*args, **kwargs)
    #     self.fields['restricted_to'].queryset = self.usergroups