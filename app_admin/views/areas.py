from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from app_base.models import Event, Area
from app_admin.forms import AreaEditForm
from . import templater


@view_function
@group_required('Manager', 'Admin')
def create(request):
    ''' Creates a new area '''
    params = {}
    form = AreaEditForm()
    if request.method == 'POST':
        form = AreaEditForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.event_id = request.urlparams[0]
            a.save()
            return HttpResponseRedirect('/app_admin/events.view/' + str(request.urlparams[0]))

    params['form'] = form
    params['title'] = 'Create Area'
    return templater.render_to_response(request, 'create_area.html', params)


@view_function
@group_required('Manager', 'Admin')
def edit(request):
    ''' Edits an area '''
    try:
        area = Area.objects.get(id=request.urlparams[0])
    except Area.DoesNotExist:
        return HttpResponseRedirect('/app_admin/events.view/' + str(request.urlparams[0]))

    params = {}
    form = AreaEditForm(instance=area)

    if request.method == 'POST':
        form = AreaEditForm(request.POST, instance=area)
        if form.is_valid():
            newform = form.save(commit=False)
            event_id = newform.event_id
            form.save()
            return HttpResponseRedirect('/app_admin/events.view/' + str(event_id))

    params['form'] = form
    params['title'] = 'Edit Area'
    return templater.render_to_response(request, 'create_area.html', params)


@view_function
@group_required('Manager', 'Admin')
def delete(request):
    ''' Deletes an area '''
    try:
        area = Area.objects.get(id=request.urlparams[0])
        event_id = area.event_id
    except Area.DoesNotExist:
        return HttpResponseRedirect('/app_admin/events.view/' + str(request.urlparams[0]))

    area.delete()
    return HttpResponseRedirect('/app_admin/events.view/' + str(event_id))