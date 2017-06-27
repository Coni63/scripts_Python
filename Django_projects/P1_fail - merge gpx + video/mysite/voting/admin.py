from django.contrib import admin
from voting.models import Game, Vote, Event, Vote_event, News

# Register your models here.
admin.site.register(Game)
admin.site.register(Vote)
admin.site.register(Event)
admin.site.register(Vote_event)
admin.site.register(News)
