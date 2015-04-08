from django_mako_plus.controller import view_function
from app_base.admin import group_required
from app_base.models import User
from . import templater


@view_function
@group_required('Manager', 'Admin')
def process_request(request):
    users = User.objects.all()
    params = {}
    params['users'] = users
    return templater.render_to_response(request, 'index.html', params)
