from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django_mako_plus.controller import view_function
from app_account.account_forms import LoginForm
from . import templater


@view_function
def loginUser(request):
    params = {}
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
                ''')

    params['form'] = form
    params['title'] = 'Log In'
    params['function'] = 'login.loginUser'
    return templater.render_to_response(request, 'form.html', params)


@view_function
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
