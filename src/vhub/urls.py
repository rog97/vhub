"""vhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from startups.views import StartupIndex

urlpatterns = [
    url(r'^$', 'vhubs.views.home', name='home'),
    url(r'^contact/$', 'vhubs.views.contact', name='contact'),
    url(r'^create/$', 'startups.views.create_view', name='create_view'),
    url(r'^startup/(?P<object_id>\d+)/$', 'startups.views.startup_view', name='startup_view'),
    url(r'^startup/(?P<slug>[\w-]+)/$', 'startups.views.startup_slug_view', name='startup_slug_view'),
    url(r'^startup/(?P<object_id>\d+)/edit/$', 'startups.views.update_view', name='update_view'),
    url(r'^index/$', 'startups.views.index', name='index'),
    url(r'^startups/index/$', StartupIndex.as_view(), name='startup_index_view'), 
    url(r'^news/$', 'vhub.views.news', name='news'),
    url(r'^analytics/$', 'vhub.views.analytics', name='analytics'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
