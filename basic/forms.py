# -*- coding:utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from django.contrib.auth.models import User




class UserForm(ModelForm):
    career = forms.CharField(label='Carrer', max_length=50)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'career']
