from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from app_base.models import Event, Area
from app_admin.forms import EventEditForm
from . import templater


@view_function
@group_required('Manager', 'Admin')
def process_request(request):
    events = Event.objects.all().order_by('start_date')
    params = {}
    params['events'] = events
    return templater.render_to_response(request, 'events.html', params)


@view_function
@group_required('Manager', 'Admin')
def create(request):
    params = {}
    form = EventEditForm()
    if request.method == 'POST':
        form = EventEditForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = form.save(commit=False)
            newimg.map_file = request.FILES['map_file']
            newimg.save()
            return HttpResponseRedirect('/app_admin/events/')

    params['form'] = form
    params['function'] = 'events.create'
    params['title'] = 'Create Event'
    return templater.render_to_response(request, 'create_event.html', params)


@view_function
@group_required('Manager', 'Admin')
def edit(request):
    try:
        event = Event.objects.get(id=request.urlparams[0])
    except Event.DoesNotExist:
        return HttpResponseRedirect('/app_admin/events/')

    params = {}
    form = EventEditForm(instance=event)

    if request.method == 'POST':
        form = EventEditForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app_admin/events/')

    params['form'] = form
    params['event'] = event
    params['function'] = 'events.edit'
    params['title'] = 'Edit Event'
    return templater.render_to_response(request, 'create_event.html', params)


@view_function
@group_required('Manager', 'Admin')
def delete(request):

    try:
        event = Event.objects.get(id=request.urlparams[0])
        areas = Area.objects.all().filter(event_id=request.urlparams[0])
    except Event.DoesNotExist:
        return HttpResponseRedirect('/app_admin/events/')

    for area in areas:
        area.delete()
    event.delete()

    return HttpResponseRedirect('/app_admin/events/')


@view_function
@group_required('Manager', 'Admin')
def view(request):
    params = {}
    try:
        params['event'] = Event.objects.get(id=request.urlparams[0])
        params['areas'] = Area.objects.all().filter(
            event_id=request.urlparams[0])
    except Event.DoesNotExist:
        return HttpResponseRedirect('/')

    return templater.render_to_response(request, 'view_event.html', params)
