from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import VideoForm
from .models import Video
from .youtube_parser import *


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


@login_required(redirect_field_name='/login/')
def BrowseVideoPage(request):
    group_list = request.user.groups.all()
    if len(group_list) > 0: # si l'utilisateur appartient a un groupe
        template = "browse.html"
        context = {'data' : Video.objects.filter(restricted_to__in=group_list)}
        return render(request, template, context)


@login_required(redirect_field_name='/login/')
def BrowseGamePage(request):
    group_list = request.user.groups.all()
    if len(group_list) > 0: # si l'utilisateur appartient a un groupe
        template = "browse.html"
        context = {'data' : Video.objects.filter(restricted_to__in=group_list)}
        return render(request, template, context)


@login_required(redirect_field_name='/login/')
def BrowseEventPage(request):
    group_list = request.user.groups.all()
    if len(group_list) > 0: # si l'utilisateur appartient a un groupe
        template = "browse.html"
        context = {'data' : Video.objects.filter(restricted_to__in=group_list)}
        return render(request, template, context)


@login_required(redirect_field_name='/login/')
def AddVideo(request):
    if request.method == 'POST':
        form = VideoForm(request.user, request.POST)
        if form.is_valid(): # and request.user.groups.all():
            video = form.save(commit=False)
            address = video.url
            print(address)
            info = request_info(address)
            video.key = info['id']
            video.name = info['title']
            video.views_counter = info['views']
            video.upload_date = info['uploaded']
            video.author = info['author']
            video.added_by = request.user
            #video.restricted_to = video.restricted_to
            video.save()
            return redirect('/browse_video/')
    else:
        group_list = request.user.groups.all()
        form = VideoForm(request.user)
    return render(request, 'add_video.html', {'form': form})