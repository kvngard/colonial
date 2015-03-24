from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django_mako_plus.controller import view_function
from app_base.forms import PasswordChangeForm
from . import templater


@view_function
def process_request(request):
    params = {}
    form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponse(
                '''
                <script>
                    window.location.href = 'window.location.href'
                </script>
                ''')

    params['form'] = form
    params['title'] = 'Change Password'
    params['function'] = 'change_password'
    return templater.render_to_response(request, 'form.html', params)
