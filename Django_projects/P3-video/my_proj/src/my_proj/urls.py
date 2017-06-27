from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^home/$', views.HomePage.as_view(), name='home'),
    url(r'^browse_video/$', views.BrowseVideoPage, name='browse_video'),
    url(r'^browse_game/$', views.BrowseGamePage, name='browse_game'),
    url(r'^browse_event/$', views.BrowseEventPage, name='browse_event'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^add_video/$', views.AddVideo, name='post video'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
