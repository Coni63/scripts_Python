from django.views import generic
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required

from .forms import GPX_fileForm
from .models import GPX_file
from .script.functions import *

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


def handler400(request):
    #response = render_to_response('error.html', {},  context_instance=RequestContext(request))
    context = {}
    context['error'] = {"title": "Error 400", "description": "La requete demande n'est pas valide"}
    response = render(request, "error.html", )
    response.status_code = 400
    return response


def handler403(request):
    #response = render_to_response('error.html', {},  context_instance=RequestContext(request))
    context = {}
    context['error'] = {"title": "Error 403", "description": "Vous n'etes pas autorisé a acceder a cette page"}
    response = render(request, "error.html", )
    response.status_code = 403
    return response


def handler404(request):
    #response = render_to_response('error.html', {},  context_instance=RequestContext(request))
    context = {}
    context['error'] = {"title": "404 Not Found", "description": "La page demandée n'existe pas :("}
    response = render(request, "error.html", )
    response.status_code = 404
    return response


def handler500(request):
    #response = render_to_response('error.html', {},  context_instance=RequestContext(request))
    context = {}
    context['error'] = {"title": "Error 500", "description": "Erreur serveur"}
    response = render(request, "error.html", )
    response.status_code = 500
    return response


@login_required(redirect_field_name='/login/')
def Upload_GPX(request):
    if request.method == 'POST':
        form = GPX_fileForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():  # and request.user.groups.all():
            entry = form.save(commit=False)
            print("valid")
            entry.added_by = request.user
            entry.save()
            print(entry.key)
            return redirect('/explore/')
    else:
        form = GPX_fileForm()
    return render(request, 'upload.html', {'form': form})


@login_required(redirect_field_name='/login/')
def Explore_my_GPX(request):
    template = "explore.html"
    context = {'data': GPX_file.objects.all()}
    return render(request, template, context)


@login_required(redirect_field_name='/login/')
def see_details(request, id):
    context = {}
    filename = id + '.gpx'
    try:
        with open(os.path.join(settings.MEDIA_ROOT, 'uploads', filename)) as f:
            context['data'] = analyse_gpx(f)
            template = "detail.html"
    except FileNotFoundError:
        context['error'] = {"title" : "404 Not Found" , "description" : "Le fichier demandé n'a pas été trouvé :(" }
        template = "error.html"
    return render(request, template, context)

try:
    with open("rien.txt") as f:
        for line in f.readlines():
            print(line)
except FileNotFoundError:
    print("fichier manquant")