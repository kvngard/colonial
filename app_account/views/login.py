from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django_mako_plus.controller import view_function
from app_account.account_forms import LoginForm
from . import templater


@view_function
def loginUser(request):
    params = {}
    redirect_app = request.REQUEST.get('redirect_app')
    redirect_func = request.REQUEST.get('redirect_func')
    title = request.REQUEST.get('title')
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password'))

            if 'shopping_cart' in request.session:
                cart = request.session['shopping_cart']
                login(request, user)
                request.session['shopping_cart'] = cart

            login(request, user)
            if request.urlparams[0] != '':
                return HttpResponse("<script> window.location.href = '/{}/{}/'</script>".format(request.urlparams[0], request.urlparams[1]))
            return HttpResponse('''
                <script>
                    window.location.href = window.location.href;
                </script>
                ''')

    if(title is None):
        title = "Log In"

    params['redirect_app'] = redirect_app
    params['redirect_func'] = redirect_func

    params['form'] = form
    params['title'] = title

    params['function'] = 'login.loginUser'

    params['option'] = 'Sign Up'
    params['option_link'] = '/app_account/new.validate_form/'

    params['option2'] = 'Forgot Password?'
    params['option2_link'] = '/password_reset/'

    return templater.render_to_response(request, 'form.html', params)


@view_function
@login_required(redirect_field_name='/')
def logoutUser(request):
    logout(request)
    if request.META:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect('/')
