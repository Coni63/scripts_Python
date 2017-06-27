from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    proposed_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    url_JVC = models.URLField()
    pochette = models.URLField()
    score = models.IntegerField(default='0')

    def upvote(self, inc = 1):
        self.score += inc
        self.save()

    def downvote(self, inc = 1):
        self.score -= inc
        self.save()

class Vote(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    vote_type = models.CharField(max_length=10, default='0')

    class Meta:
        unique_together = ('user', 'game', 'vote_type')


class Event(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=True, blank=True)
    proposed_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    game = models.CharField(max_length=50, default="", null=True, blank=True)
    url = models.URLField(default="", null=True, blank=True)
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    stop = models.DateTimeField(auto_now=False, auto_now_add=False)


class Vote_event(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    vote_type = models.CharField(max_length=10, default='0')

    class Meta:
        unique_together = ('user', 'event', 'vote_type')

class News(models.Model):
    proposed_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField(auto_now=True)
    version = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = models.TextField()