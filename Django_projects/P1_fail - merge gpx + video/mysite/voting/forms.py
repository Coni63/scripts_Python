#from django.forms import ModelForm
from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from voting.models import Game, Event
from django.db import models
from django.contrib.auth.models import User
#from django.contrib.admin import widgets
from datetimewidget.widgets import DateTimeWidget
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'style', 'price', 'url_JVC', 'pochette']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "price", "game", "url", "start", "stop"]
        widgets = {
                    'start': DateTimeWidget(usel10n=True, bootstrap_version=3),
                    'stop': DateTimeWidget(usel10n=True, bootstrap_version=3)
                    }

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        debut = cleaned_data.get("start")
        fin = cleaned_data.get("stop")

        if fin <= debut:
            msg = "La date de fin doit etre plus tard que celle du debut"
            self.add_error('stop', msg)


class UpdateProfile(forms.ModelForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
