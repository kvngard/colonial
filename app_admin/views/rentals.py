from django.contrib.auth.decorators import permission_required
from django_mako_plus.controller import view_function
from app_base.widgets import CheckboxSelectMultiple
from app_store.storeforms import Credit_Card_Form
from django.http import HttpResponseRedirect
from app_base.forms import site_model_form
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
            date_due__lte=datetime.date.today(),
            date_out__exact=None)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    rentals_to_check_out = []
    request.session['rentals_to_check_out'] = []
    user = None
    total = 0

    if request.method == 'POST':

        data = dict(request.POST)

        for rental in rentals:
            if data.get(str(rental.id))[0]:
                if data.get(str(rental.id))[0] == 'on':

                    rentals_to_check_out.append(rental)
                    request.session['rentals_to_check_out'].append(str(rental.id))

                    total += rental.checkout_price
                    user = rental.transaction.customer

        params['total'] = total
        params['rentals'] = rentals_to_check_out
        params['credit_card_form'] = Credit_Card_Form()

        return templater.render_to_response(request, '/app_store/templates/checkout.html', params)


    params['title'] = "Checkout Rentals"
    params['rentals'] = rentals

    return templater.render_to_response(request, 'checkout_rentals.html', params)


@view_function
def charge(request):

    if request.method == "POST":
        params = {}

        try:
            rentals = mod.Rental.objects.filter(id__in=request.session['rentals_to_check_out'])
        except mod.Rental.DoesNotExist:
            return HttpResponseRedirect('/')

        request.session['rentals_to_check_out'] = []

        data = dict(request.POST)
        total = 0

        for rental in rentals:
            total += rental.checkout_price
            user = rental.transaction.customer

        credit_card_form = Credit_Card_Form(request.POST, total=total, user=user)

        if credit_card_form.is_valid():
            for r in rentals:

                t = r.transaction
                r.date_out = datetime.date.today()
                r.date_due = datetime.date.today() + datetime.timedelta(r.duration)
                r.handled_by = request.user
                r.save()

                p = mod.Payment()
                p.amount = r.checkout_price
                p.transaction = t
                p.charge_id = credit_card_form.resp['ID']
                p.save()

            params['rentals'] = rentals
            params['total'] = total

            return templater.render_to_response(request, '/app_store/templates/checkout_receipt.html', params)

    HttpResponseRedirect('/app_admin/rentals.checkout/')


@view_function
def late(request):
    params = {}

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

    params['rentals'] = rentals
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

    emailbody = templater.render(request, 'rental_report_email.html', params)

    send_mail(
        'Colonial Heritage Foundation - Overdue Report',
        emailbody,
        'chfsite@gmail.com',
        [request.user.email],
        html_message=emailbody,
        fail_silently=False
    )

    return templater.render_to_response(request, 'rental_report.html', params)


@view_function
def check_in(request):
    params = {}
    id = request.urlparams[0]

    return_form = Return_Form()
    damage_form = Damage_Form()

    try:
        rental = mod.Rental.objects.get(id=id)
    except mod.Rental.DoesNotExist:
        return HttpResponseRedirect('/')

    if request.method == "POST":
        return_form = Return_Form(request.POST)
        damage_form = Damage_Form(request.POST)

        if damage_form.is_valid():
            damange_form.save()

        if return_form.is_valid():
            rr = hmod.Rental_Return()
            rr.return_condition = return_form.cleaned_data['return_condition'],
            rr.date_in = datetime.date.today()
            rr.rental= rental
            rr.handled_by = request.user
            rr.save()

            if rr.date_in > rental.date_due:
                print(rr.date_in - rental.date_due)

        HttpResponseRedirect('/app_admin/rentals.late/')

    params['rental'] = rental
    params['return_form'] = return_form
    params['damage_form'] = damage_form

    return templater.render_to_response(request, 'return_rental.html', params)


class Return_Form(site_model_form):

    class Meta:
        model = mod.Rental_Return
        fields = ['return_condition']
        widgets = {
            'return_condition': CheckboxSelectMultiple(),
        }


class Damage_Form(site_model_form):

    class Meta:
        model = mod.Damage_Fee
        fields = ['description','amount']
