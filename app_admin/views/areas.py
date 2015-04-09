from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from app_base.models import Event, Area
from app_admin.forms import AreaEditForm
from . import templater


@view_function
@group_required('Manager', 'Admin')
def create(request):
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
    try:
        area = Area.objects.get(id=request.urlparams[0])
    except Area.DoesNotExist:
        return HttpResponseRedirect('/')

    params = {}
    form = AreaEditForm(instance=area)

    if request.method == 'POST':
        form = AreaEditForm(request.POST, request.FILES, instance=area)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    params['form'] = form
    params['title'] = 'Edit Area'
    return templater.render_to_response(request, 'create_area.html', params)


@view_function
@group_required('Manager', 'Admin')
def delete(request):

    try:
        area = Area.objects.get(id=request.urlparams[0])
        event_id = area.event_id
    except Area.DoesNotExist:
        return HttpResponseRedirect('/app_admin/events/')

    area.delete()
    return HttpResponseRedirect('/app_admin/events.view/' + str(event_id))


@view_function
@group_required('Manager', 'Admin')
def view(request):
    params = {}
    try:
        area = Area.objects.get(id=request.urlparams[0])
        areas = Area.objects.all().filter(
            area_id=request.urlparams[0]).order_by('id')
    except Area.DoesNotExist:
        return HttpResponseRedirect('/app_admin/areas/')

    params['area'] = area
    params['areas'] = areas
    return templater.render_to_response(request, 'view_area.html', params)
