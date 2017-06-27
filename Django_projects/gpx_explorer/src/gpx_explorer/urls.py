from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/$', views.Upload_GPX, name='upload'),
    url(r'^explore/$', views.Explore_my_GPX, name='explore'),
    url(r'^detail/(\w{32})/$', views.see_details, name='details'),
    url(r'^', include(accounts.urls, namespace='accounts')),
]

handler400 = 'gpx_explorer.views.handler400'
handler403 = 'gpx_explorer.views.handler403'
handler404 = 'gpx_explorer.views.handler404'
handler500 = 'gpx_explorer.views.handler500'

#rRXVe68NO7m3mHoBS488KdHaqQPD6Ofv
# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
