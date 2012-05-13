#!/usr/bin/env python
#!-*- coding: utf-8 -*-

from django.contrib import admin
from auto1.models import Server, ServerGroup, Project

class ServerGroupAdmin ( admin.ModelAdmin ):
    pass

class ServerAdmin ( admin.ModelAdmin ):
    pass

class ProjectAdmin ( admin.ModelAdmin ):
    pass

admin.site.register ( Server, ServerAdmin )
admin.site.register ( ServerGroup, ServerGroupAdmin )
admin.site.register ( Project, ProjectAdmin )
