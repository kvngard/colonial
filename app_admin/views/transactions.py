from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_base.admin import group_required
import app_base.models as mod
from . import templater


@view_function
@group_required('Manager', 'Admin')
def process_request(request):
	'''
        method for getting transactions
    '''
    params = {}

    try:
        transactions = mod.Transaction.objects.all()
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/app_admin/')

    params['transactions'] = transactions

    return templater.render_to_response(request, 'transactions.html', params)
