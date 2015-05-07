__author__ = 'Rebeca'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from basic.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Team, TeamMember, Role, TeamRole


class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = ('active', )



class TeamMemberForm(ModelForm):
    class Meta:
        model = TeamMember
        exclude = ('active', )


class RoleForm(ModelForm):
    class Meta:
        model = Role
        exclude = ('active',)



class TeamRoleForm(ModelForm):
    user = forms.CharField(label='User', max_length=100)

    def clean(self):
        cleaned_data = super(TeamRoleForm, self).clean()
        print cleaned_data
        username = cleaned_data.get("user")
        user = User.objects.all().filter(user__username=username)
        print user
        if not user.count():
            message = u"User does not exist" 
            self.add_error('user', message)

        return self.cleaned_data

    class Meta:
        model = TeamRole
        exclude = ('active', 'user')