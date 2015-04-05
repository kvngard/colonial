from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
import app_base.models as mod
from . import templater


@view_function
def process_request(request):
    params = {}
    event_name = request.urlparams[0]
    event = mod.Event.objects.get(name=event_name)
    params['event'] = event

    return templater.render_to_response(request, 'details.html', params)