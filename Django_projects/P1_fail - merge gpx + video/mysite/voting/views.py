from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import filesizeformat
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Game, Vote, News, Event
from .forms import GameForm, UpdateProfile, EventForm


def is_active(person):
	if person.groups.filter(name='approved').exists():
		return True
	else:
		return False


@login_required
def home(request):
	return render(request, 'voting/home.html', {"is_active": is_active(request.user)})


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			user.save()
			login(request, user)
			return redirect('/home')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html', {'form': form})


@login_required
def game(request):
    vote_made = Vote.objects.all().filter(user = request.user)
    vote_obj = {}
    for each in vote_made:
        vote_obj[each.game.id] = each.vote_type
    print(vote_obj)
    return render(request, 'voting/game.html', {"is_active": is_active(request.user), "games": Game.objects.all(), "votes":vote_obj})


@login_required
def addgame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.proposed_by = request.user
            game.save()
            return redirect('/home')
    else:
        form = GameForm()
    return render(request, 'voting/addgame.html', {"is_active": is_active(request.user), 'form': form})


@login_required
def event(request):
	return render(request, 'voting/event.html', {"is_active": is_active(request.user), "events": Event.objects.all()})


@login_required
def addevent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.proposed_by = request.user
            event.save()
            return redirect('/event')
    else:
        form = EventForm()
    return render(request, 'voting/addevent.html', {"is_active": is_active(request.user), 'form': form})


@login_required
def profil(request):
	args = {"email":request.user.email, "last_name":request.user.last_name, "first_name":request.user.first_name}
	if request.method == 'POST':
		form = UpdateProfile(request.POST, initial=args)
		current_user = request.user
		if form.is_valid():
			current_user.first_name = form.cleaned_data['first_name']
			current_user.last_name = form.cleaned_data['last_name']
			current_user.email = form.cleaned_data['email']
			current_user.save()
			return redirect('/home')
	else:
		form = UpdateProfile(args)
	return render(request, 'voting/profil.html', {"form": form})


@login_required
def userlist(request):
	return render(request, 'voting/userlist.html', {"is_active": is_active(request.user), "users": User.objects.all()})


@login_required
def vote(request):
    _user = request.user
    _target = request.GET.get('_target', None)
    _type = request.GET.get('_type', None)
    if not _target is None and not _type is None:
        _game = Game.objects.get(pk=_target)
        print(_user, _game, _type)
        if Vote.objects.filter(user=_user, game=_game).count() > 0:
            vote_concerned = Vote.objects.get(user=_user, game=_game)
            old_vote = vote_concerned.vote_type
            if old_vote == "0" and _type == "up":
                vote_concerned.vote_type = "up"
                vote_concerned.save()
                _game.upvote()
                data = {'status': 4}  # vote changed
            elif old_vote == "0" and _type == "down":
                vote_concerned.vote_type = "down"
                vote_concerned.save()
                _game.downvote()
                data = {'status': 4}  # vote changed
            elif old_vote == "up" and _type == "up":
                vote_concerned.vote_type = "0"
                vote_concerned.save()
                _game.downvote()
                data = {'status': 1}  # vote removed
            elif old_vote == "up" and _type == "down":
                vote_concerned.vote_type = "down"
                vote_concerned.save()
                _game.downvote(2)
                data = {'status': 4}  # vote changed
            elif old_vote == "down" and _type == "up":
                vote_concerned.vote_type = "up"
                vote_concerned.save()
                _game.upvote(2)
                data = {'status': 4}  # vote changed
            elif old_vote == "down" and _type == "down":
                vote_concerned.vote_type = "0"
                vote_concerned.save()
                _game.upvote()
                data = {'status': 1}  # vote removed
        else:
            v = Vote(user = _user, game = _game, vote_type = _type)
            if _type == "up":
                _game.upvote()
            else:
                _game.downvote()
            v.save()
            data = {'status': 2 } #vote added
    else:
        data = {'status': 3} #error

    return JsonResponse(data)

@login_required
def news(request):
    return render(request, 'voting/news.html', {"is_active": is_active(request.user), "news": News.objects.order_by("-date")})