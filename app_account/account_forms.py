from django import forms
from django.contrib.auth import authenticate
from app_base.models import User


class LoginForm(forms.Form):
    username = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(username=self.cleaned_data.get(
            'username'), password=self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError(
                "Sorry, that's not an existing email-password combination.")


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'profile_image', 'security_question',
                  'security_answer', 'phone']
