from django.http import HttpResponseRedirect
from django_mako_plus.controller import view_function
from app_account.account_forms import UserEditForm
from app_base.models import User
from . import templater


@view_function
def process_request(request):
    try:
        user = User.objects.get(id=request.user.id)
    except User.DoesNotExist:
        return HttpResponseRedirect('/')

    params = {}
    form = UserEditForm(instance=user)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    params['form'] = form
    params['title'] = 'Account'
    return templater.render_to_response(request, 'manage.html', params)
