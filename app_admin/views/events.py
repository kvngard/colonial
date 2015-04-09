from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from app_base.models import Event
from app_admin.forms import EventEditForm
from . import templater


@view_function
@group_required('Manager')
def process_request(request):
    events = Event.objects.all()
    params = {}
    params['events'] = events
    return templater.render_to_response(request, 'events.html', params)


@view_function
@group_required('Manager')
def create(request):
    params = {}
    form = EventEditForm()
    if request.method == 'POST':
        print(request.FILES)
        form = EventEditForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = form.save(commit=False)
            newimg.map_file = request.FILES['map_file']
            newimg.save()
            return HttpResponseRedirect('/app_admin/events/')

    params['form'] = form
    params['title'] = 'Create Event'
    return templater.render_to_response(request, 'create_event.html', params)


@view_function
@group_required('Manager')
def edit(request):
    try:
        event = Event.objects.get(id=request.urlparams[0])
    except Event.DoesNotExist:
        return HttpResponseRedirect('/')

    params = {}
    form = EventEditForm(instance=event)

    if request.method == 'POST':
        form = EventEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    params['form'] = form
    params['title'] = 'Edit Event'
    return templater.render_to_response(request, 'create_event.html', params)


@view_function
@group_required('Manager')
def delete(request):

    try:
        event = Event.objects.get(id=request.urlparams[0])
    except Event.DoesNotExist:
        return HttpResponseRedirect('/app_admin/events/')

    event.delete()

    return HttpResponseRedirect('/app_admin/events/')
