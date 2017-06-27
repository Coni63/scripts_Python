from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name = "index"),
    url(r'^home', views.home, name = "index"),
    url(r'^game', views.game, name = "index"),
    url(r'^addgame', views.addgame, name = "index"),
    url(r'^event', views.event, name = "index"),
    url(r'^addevent', views.addevent, name = "index"),
    url(r'^profil', views.profil, name = "index"),
    url(r'^userlist', views.userlist, name = "index"),
    url(r'^login$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^ajax/vote/$', views.vote, name='vote'),
    url(r'^news/$', views.news, name='vote'),
]