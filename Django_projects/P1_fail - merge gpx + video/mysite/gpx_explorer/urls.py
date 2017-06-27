from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.home, name = "index"),
    url(r'^home', views.home, name = "index"),
    url(r'^tutorial', views.tutorial, name = "index"),
    url(r'^about_me', views.about_me, name = "contact"),
    url(r'^upload', views.upload_file, name = "contact"),
    url(r'^analyse', views.analyse, name = "contact"),
    url(r'^contact', views.contact, name = "contact"),
    url(r'^generate', views.export_pdf, name = "contact"),
]