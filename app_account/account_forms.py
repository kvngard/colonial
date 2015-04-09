from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
from ldap3.core.exceptions import LDAPBindError, LDAPPasswordIsMandatoryError, LDAPSocketOpenError
from app_base.widgets import MaterializeClearableFileInput
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from app_base.forms import site_form
from app_base.models import User
from django import forms


class LoginForm(site_form):
    username = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):

        try:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is None or user.is_staff is True:

                try:

                    # Shortens the username for use with LDAP. A user MUST have the
                    # same username as their email username.
                    if '@' in username:
                        username = username.split('@')[0]

                    # Open connection with the LDAP server.
                    s = Server(
                        'colonialheritagefoundation.org', port=8889, get_info=GET_ALL_INFO)
                    c = Connection(s, auto_bind=True, client_strategy=STRATEGY_SYNC, user='COLONIAL\\{}'.format(username),
                                   password=password, authentication=AUTH_SIMPLE, raise_exceptions=False)

                    # LDAP query to get user attributes.
                    c.search(
                        search_base='CN=Users,DC=colonialheritagefoundation,DC=local',
                        search_filter='(samAccountName={})'.format(username),
                        attributes=['samAccountName', 'givenName', 'sn', 'mail', ]
                    )

                    # Parse the LDAP query response to get the user_info
                    # dictionary.
                    user_info = c.response[0]['attributes']

                    if user_info['samAccountName'] != username:
                        raise forms.ValidationError(
                        "Sorry, that's not an existing email-password combination.")

                    c.unbind()

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
                except LDAPPasswordIsMandatoryError as ldape:
                    print(ldape)
                    raise forms.ValidationError(
                        "Please include as password.")
                except LDAPSocketOpenError as e:
                    print(e)
                    c.unbind()

        except KeyError as e:
            print(e)


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'profile_image']
        widgets = {
            'profile_image': MaterializeClearableFileInput(attrs={'class': 'upload-btn'}),
        }
