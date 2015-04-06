from django.contrib.auth.decorators import permission_required
from django_mako_plus.controller import view_function
from app_account.account_forms import UserEditForm
from app_base.forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from app_base.models import User
from django import forms
from . import templater


@view_function
def process_request(request):
    users = User.objects.all()
    params = {}
    params['users'] = users
    return templater.render_to_response(request, 'users.html', params)


@view_function
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
def edit(request):
    try:
        user = User.objects.get(id=request.urlparams[0])
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
    params['title'] = 'Edit User'
    return templater.render_to_response(request, 'edit_user.html', params)


@view_function
def delete(request):

    try:
        user = User.objects.get(id=request.urlparams[0])
    except User.DoesNotExist:
        return HttpResponseRedirect('/app_admin/users/')

    user.delete()

    return HttpResponseRedirect('/app_admin/users/')
