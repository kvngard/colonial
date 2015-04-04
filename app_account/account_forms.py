from django import forms
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
from ldap3.core.exceptions import LDAPBindError
from app_base.forms import site_model_form, site_form
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from app_base.models import User
from app_base.widgets import CheckboxSelectMultiple
import json


class LoginForm(site_form):
    username = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is None or user.is_staff is True:

            try:

                # Shortens the username for use with LDAP. A user MUST have the same username as their email username.
                if '@' in username:
                    username = username.split('@')[0]

                # Open connection with the LDAP server.
                s = Server(
                    'colonialheritagefoundation.org', port=8889, get_info=GET_ALL_INFO)
                c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user='COLONIAL\\{}'.format(username),
                               password=password, authentication=AUTH_SIMPLE, raise_exceptions=False)

                # LDAP query to get user attributes.
                search_results = c.search(
                    search_base='CN=Users,DC=colonialheritagefoundation,DC=local',
                    search_filter='(samAccountName={})'.format(username),
                    attributes=['givenName', 'sn', 'mail', ]
                )

                # Parse the LDAP query response to get the user_info dictionary.
                user_info = json.loads(c.response_to_json(search_results))['entries'][0]['attributes']

                if user is None:

                    user = User()
                    user.first_name = user_info['givenName']
                    user.last_name = user_info['sn']
                    user.email = user_info['mail']
                    user.username = username
                    user.is_staff = True

                    user.set_password(password)
                    user.save()

                    Group.objects.get(name='Manager').user_set.add(user)

            except LDAPBindError as ldape:
                print(ldape)
                raise forms.ValidationError(
                    "Sorry, that's not an existing email-password combination.")


class UserEditForm(site_model_form):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'groups']
        widgets = {
            'groups': CheckboxSelectMultiple(),
        }
