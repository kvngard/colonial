from django.contrib.auth.decorators import permission_required
from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
import app_base.models as mod
from . import templater
import datetime


@view_function
@permission_required('manager_rights')
def late(request):
    params = {}

    try:
        rentals = mod.Rental.objects.filter(
            date_due__lt=datetime.date.today(), return_instance__iexact=None)
    except mod.Sale_Product.DoesNotExist:
        return HttpResponseRedirect('/')

    dayslate = {}
    for rental in rentals:
        today = datetime.datetime.today().replace(tzinfo=None)
        due_date = rental.date_due.replace(tzinfo=None)
        delta = today - due_date
        dayslate[rental.rental_item.name] = delta.days

    params['rentals'] = rentals
    params['dayslate'] = dayslate

    return templater.render_to_response(request, 'late_rentals.html', params)
