from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import filesizeformat
from .models import GPX_File, Contact_Form

from reportlab.pdfgen import canvas
from django.http import HttpResponse

import os

from .script.functions import analyse_gpx
from .forms import UploadFileForm, ContactForm

def home(request):
    return render(request, 'gpx_explorer/home.html')


def tutorial(request):
	return render(request, 'gpx_explorer/tutorial.html')


def about_me(request):
	return render(request, 'gpx_explorer/about_me.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['last_file_uploaded_ID'] = form.instance.id
            return render(request, 'gpx_explorer/analyse.html')
    else:
        form = UploadFileForm()
    return render(request, 'gpx_explorer/upload.html', {'form': form})


def analyse(request):
    id_file = request.session.get('last_file_uploaded_ID', None)

    if id_file is None:
        upload_file(request)
    else:
        obj = GPX_File.objects.get(pk=id_file)
        f = open(obj.file.path, "r")
        data = analyse_gpx(f, id_file)
        return render(request, 'gpx_explorer/analyse.html', {"data":data, "id_file":id_file})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,  request.FILES)
        if form.is_valid():
            #form.save()
            #request.session['last_file_uploaded_ID'] = form.instance.id
            #return render(request, 'gpx_explorer/analyse.html')
            return render(request, 'gpx_explorer/home.html')
    else:
        form = ContactForm()
    return render(request, 'gpx_explorer/contact.html', {'form': form})


def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response