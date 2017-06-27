from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat

from .models import GPX_File, Contact_Form

def validate_file_extension(value):
    if not value.name.endswith('.gpx'):
        raise forms.ValidationError(u'Unsupported file extension. (.gpx files only)')
    if value.size > settings.MAX_UPLOAD_SIZE:
        raise forms.ValidationError(u'Please keep filesize under %s. Current filesize %s' % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(value.size)))


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = GPX_File
        fields = ['title', 'file']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Form
        fields = ['mail', 'subject', 'content']