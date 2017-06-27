from django.views import generic
from django.shortcuts import render, redirect
from .forms import VideoForm
from .models import Video

class HomePage(generic.TemplateView):
    template_name = "home.html"

def BrowsePage(request):
    template = "browse.html"
    context = {'data' : Video.objects.all()}
    return render(request, template, context)

def AddVideo(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.added_by = request.user
            video.save()
            return redirect('/browse/')
    else:
        form = VideoForm()
    return render(request, 'add_video.html', {'form': form})

class AboutPage(generic.TemplateView):
    template_name = "about.html"

def get_vids_info(request):
    if request.method == 'POST':
        template = "browse.html"
        context = {'data': Video.objects.all()}
        return render(request, template, context)

