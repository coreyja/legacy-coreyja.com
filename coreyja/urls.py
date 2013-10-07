from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from main.views import HomeView, ProjectView

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coreyja.views.home', name='home'),
    # url(r'^coreyja/', include('coreyja.foo.urls')),

    url(r'^$', HomeView.as_view(), {'page': 1}, name="home"),
    url(r'^(?P<page>\d+)/$', HomeView.as_view(), name="home_paginated"),

    url(r'^project/(?P<slug>[\w-]+)/$', ProjectView.as_view(), name="project"),
    url(r'^resume/$', TemplateView.as_view(template_name="resume.html"), name="project"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns.append(url(r"%s(?P<path>.*)$" % settings.MEDIA_URL[1:], "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}))
