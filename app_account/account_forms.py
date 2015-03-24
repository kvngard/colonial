from django import forms
from app_base.forms import site_model_form, site_form
from django.contrib.auth import authenticate
from app_base.models import User
from app_base.widgets import CheckboxSelectMultiple


class LoginForm(site_form):
    username = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(username=self.cleaned_data.get(
            'username'), password=self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError(
                "Sorry, that's not an existing email-password combination.")


class UserEditForm(site_model_form):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'groups']
        widgets = {
            'groups': CheckboxSelectMultiple(),
        }
