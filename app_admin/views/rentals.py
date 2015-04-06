from django.contrib.auth.decorators import permission_required
from django_mako_plus.controller import view_function
from django.http import HttpResponseRedirect
from app_store.storeforms import Credit_Card_Form
from django.core.mail import send_mail
import app_base.models as mod
from django import forms
from . import templater
import datetime

@view_function
def checkout(request):
    params = {}

    try:
        rentals = mod.Rental.objects.filter(
            checkout_by_date__gte=datetime.date.today(),
            date_out__exact=None)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    if request.method == 'POST':

        print(request.POST)
        '''credit_card_form = Credit_Card_Form(request.POST, total=total, user=request.user)

        if address_form.is_valid() and credit_card_form.is_valid():
            a = address_form.save()
            t = create_transaction(request, credit_card_form.resp, total, a)
            return HttpResponseRedirect('/app_store/checkout.receipt/{}'.format(t.id))'''

    params['title'] = "Checkout Rentals"
    params['rentals'] = rentals

    return templater.render_to_response(request, 'checkout_rentals.html', params)

@view_function
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> master
def process_request(request):
=======
def late(request):
>>>>>>> master
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
        today = datetime.date.today()
        due_date = rental.date_due.date()
        delta = today - due_date
        dayslate[rental.rental_item.name] = delta.days

    params['rentals'] =rentals
    params['dayslate'] = dayslate

    return templater.render_to_response(request, 'late_rentals.html', params)

@view_function
def report(request):

    params = {}

    try:
        rentals = mod.Rental.objects.filter(
            date_due__lt=datetime.date.today(),
            return_instance__iexact=None)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    ninety, sixty, thirty, new = [], [], [], []

    dayslate = {}

    for rental in rentals:
        today = datetime.date.today()
        due_date = rental.date_due.date()
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

    params['rentals'] = rentals
    params['dayslate'] = dayslate
    params['ninety'] = ninety
    params['sixty'] = sixty
    params['thirty'] = thirty
    params['new'] = new

<<<<<<< HEAD
    emailbody = templater.render(request, 'late_rentals_email.html', params)
    print(request.user.email)
    print(send_mail(
        'Colonial Heritage Foundation',
=======
    emailbody = templater.render(request, 'rental_report_email.html', params)

    send_mail(
        'Colonial Heritage Foundation - Receipt',
>>>>>>> master
        emailbody,
        'chfsite@gmail.com',
        [request.user.email],
        html_message=emailbody,
        fail_silently=False
    )

    return templater.render_to_response(request, 'rental_report.html', params)

@view_function
<<<<<<< HEAD

=======
>>>>>>> master
def return_rental(request):
    params = {}
    rental = request.urlparams[0]

    return_form = Return_Form()
    damage_form = Damage_Form()

    try:
        rental = mod.Rental.objects.get(id=rental)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    params['return_form'] = return_form
    params['damage_form'] = damage_form

    return templater.render_to_response(request, 'return_rental.html', params)

class Return_Form(forms.ModelForm):

    class Meta:
        model = mod.Rental_Return

class Damage_Form(forms.ModelForm):

    class Meta:
        model = mod.Damage_Fee