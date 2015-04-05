from django.contrib.auth.decorators import permission_required
from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import app_base.models as mod
from . import templater
import datetime


@view_function
@permission_required('manager_rights')
def process_request(request):
    params = {}
    days_late_filter = request.urlparams[0]

    try:
        rentals = mod.Rental.objects.filter(
            date_due__lt=datetime.date.today(),
            return_instance__iexact=None)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    ninety = []

    sixty = []

    thirty = []

    new = []

    dayslate = {}

    for rental in rentals:
        today = datetime.datetime.today().replace(tzinfo=None)
        due_date = rental.date_due.replace(tzinfo=None)
        delta = today - due_date
        dayslate[rental.rental_item.name] = delta.days

        if delta.days < 30:
            new.append(rental)
        elif delta.days >= 30 and delta.days < 60:
            thirty.append(rental)
        elif delta.days >= 60 and delta.days < 90:
            sixty.append(rental)
        else:
            ninety.append(rental)

    params['new'] = new
    params['thirty'] = thirty
    params['sixty'] = sixty
    params['ninety'] = ninety
    params['dayslate'] = dayslate

    emailbody = templater.render(request, 'late_rentals_email.html', params)
    print(request.user.email)
    print(send_mail(
        'Colonial Heritage Foundation - Receipt',
        emailbody,
        'store@colonialheritagefoundation.org',
        [request.user.email],
        html_message=emailbody,
        fail_silently=False
    ))

    return templater.render_to_response(request, 'late_rentals.html', params)

@view_function
@permission_required('manager_rights')
def return_rental(request):
    params = {}
    days_late_filter = request.urlparams[0]

    try:
        rentals = mod.Rental.objects.filter(
            date_due__lt=datetime.date.today(),
            return_instance__iexact=None)
    except mod.Rental.DoesNotExist:
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