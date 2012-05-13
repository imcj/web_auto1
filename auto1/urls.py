from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('auto1.views',
    url ( r'^$', 'default', name = 'auto1_default' ),
    url ( r'^project/create/$', 'auto1_project_create', name = 'auto1_project_create' ),
    url ( r'^project/$', 'auto1_project_list', name = 'auto1_project_list' ),
    url ( r'^server/create/$', 'auto1_server_create', name = 'auto1_server_create' ),
    url ( r'^server/$', 'auto1_server_list', name = 'auto1_server_list' ),
)
