from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django_mako_plus.controller import view_function
from app_base.forms import CustomUserCreationForm
from . import templater


@view_function
def validate_form(request):
    params = {}
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get(
                'email'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return HttpResponse(
                '''
                <script>
                    window.location.href = window.location.href
                </script>
                ''')

    params['form'] = form
    params['title'] = 'Sign Up'
    params['function'] = 'new.validate_form'
    return templater.render_to_response(request, 'form.html', params)
