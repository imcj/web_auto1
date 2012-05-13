#!/usr/bin/env python
#! -*- coding:utf-8 -*-

from django import forms
from bootstrap.forms import BootstrapMixin
from auto1.models import Task

class TaskCreationFormMixin ( forms.ModelForm ):
    class Meta:
        fields = ( "name", )
