from django_mako_plus.controller import view_function
from app_admin.forms import Return_Form, Damage_Form
from app_store.storeforms import Credit_Card_Form
from django.http import HttpResponseRedirect
from app_base.admin import group_required
from django.core.mail import send_mail
import app_base.models as mod
from decimal import Decimal
from . import templater
import datetime


@view_function
@group_required('Manager', 'Admin')
def process_request(request):
    '''
        method for showing sales, rentals, payments, transaction
    '''
    params = {}

    try:
        transactions = mod.Transaction.objects.all()
        payments = mod.Payment.objects.all()
        sales = mod.Sale.objects.all()
        rentals = mod.Rental.objects.all()
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/app_admin/')

    params['transactions'] = transactions
    params['payments'] = payments
    params['sales'] = sales
    params['rentals'] = rentals

    return templater.render_to_response(request, 'payments.html', params)
