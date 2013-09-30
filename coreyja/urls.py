from django.conf.urls import patterns, include, url

from main.views import HomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coreyja.views.home', name='home'),
    # url(r'^coreyja/', include('coreyja.foo.urls')),

    url(r'^$', HomeView.as_view(), name="home"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
