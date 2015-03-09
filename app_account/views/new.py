from django.http import HttpResponse
from django_mako_plus.controller import view_function
from app_base.admin import CustomUserCreationForm
from . import templater


@view_function
def validate_form(request):
    params = {}
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                '''
                <script>
                    window.location.href = '/'
                </script>
                ''')

    params['form'] = form
    params['title'] = 'Sign Up'
    params['function'] = 'new.validate_form'
    return templater.render_to_response(request, 'form.html', params)
