from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'konstrukt.views.home'),
    (r'^models/(?P<id>[0-9])/$', 'konstrukt.views.view_model'),
    (r'^views/(?P<id>[0-9])/$', 'konstrukt.views.view_view'),
    url(r'^admin/', include(admin.site.urls)),
)
