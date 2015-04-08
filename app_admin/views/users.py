from django_mako_plus.controller import view_function
from app_base.forms import CustomUserCreationForm
from app_admin.forms import ManagerUserEditForm
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from app_base.models import User
from . import templater


@view_function
@group_required('Manager')
def process_request(request):
    users = User.objects.all()
    params = {}
    params['users'] = users
    return templater.render_to_response(request, 'users.html', params)


@view_function
@group_required('Manager')
def create(request):
    params = {}
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app_admin/users/')

    params['form'] = form
    params['title'] = 'Create User'
    return templater.render_to_response(request, 'create_user.html', params)


@view_function
@group_required('Manager')
def edit(request):
    try:
        user = User.objects.get(id=request.urlparams[0])
    except User.DoesNotExist:
        return HttpResponseRedirect('/')

    params = {}
    form = ManagerUserEditForm(instance=user)

    if request.method == 'POST':
        form = ManagerUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    params['form'] = form
    params['title'] = 'Edit User'
    return templater.render_to_response(request, 'edit_user.html', params)


@view_function
@group_required('Manager')
def delete(request):

    try:
        user = User.objects.get(id=request.urlparams[0])
    except User.DoesNotExist:
        return HttpResponseRedirect('/app_admin/users/')

    user.delete()

    return HttpResponseRedirect('/app_admin/users/')
